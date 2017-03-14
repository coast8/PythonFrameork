# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin
from yawdadmin import admin_site

from noticias.models import Categoria, Noticias, Album, Link, Eventos, VideoNoticia
from noticias.forms import BuscarLocalEvento, BuscarCantorAlbum


def noticiadestaque_on(modeladmin, request, queryset):
    queryset.update(destaque=True)
noticiadestaque_on.short_description = "Marcar notícias como destaque"

def noticiadestaque_off(modeladmin, request, queryset):
    queryset.update(destaque=False)
noticiadestaque_off.short_description = "Desmarcar notícias como destaque"

def noticiapublicar_on(modeladmin, request, queryset):
    queryset.update(publicar=True)
noticiapublicar_on.short_description = "Publicar notícia do site"

def noticiapublicar_off(modeladmin, request, queryset):
    queryset.update(publicar=False)
noticiapublicar_off.short_description = "Despublicar notícia do site"
#Admin Notícia
class CategoriaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações',{'fields':('nome','descricao')}),
    ]
    list_display = ['nome','descricao']

class VideoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principais', {'fields':(('publicar'),('titulo'), ('conteudo'),)}),
        ('Mídia', {'fields':('url','imagem')}),
    ]
    list_display = ['titulo', 'cliques']
    list_filter = ['publicar']
    search_fields = ['titulo']
    save_on_top= True

class EventoAdminInline(admin.StackedInline):
    form = BuscarLocalEvento
    model = Eventos
    extra = 1
    max_num = 1
    collapse = False
    description = 'Descreva informações sobre o evento'
    modal = True
    fieldsets = [
        ('Evento', {'fields': ('dataevento', 'categoria',  'local', 'ingressos', 'organizacao', 'cidade')})
    ]


class AlbumInline(admin.TabularInline):
    fieldsets = [
        ('Extras', {'fields': ('cantor_nome', 'ano', 'imagem'), 'classes':['collapse']})
    ]
    model = Album
    max_num = 1
    extra = 0

class VideoInlineAdmin(admin.TabularInline):
    fieldsets = [
        ('Extras', {'fields': ('usarvideo', 'url'), 'classes':['collapse']})
    ]
    model = VideoNoticia
    description = 'Insira o vídeo na notícia'
    max_num = 1
    extra = 1

class VideoNoticiaAdmin(admin.TabularInline):
    fieldsets = [
        ('Extras', {'fields': ('usarvideo', 'url'), 'classes':['collapse']})
    ]
    model = VideoNoticia
    max_num = 1
    extra = 1

class BaseNoticiaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Conteudo', {'fields':('conteudo', 'categoria_nome','imagem', 'fonte')}),
    ]

class NoticiaAdmin(admin.ModelAdmin):
    class Media:
        js = ("/static/yawd-admin/js/jquery.min.js",
              "/static/administrador/js/ocultar-admin.js",
        )
    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return [
                ('Principais', {'fields':(('publicar','destaque'),('titulo','subtitulo'), 'chamada')}),
                ('Principais', {'fields':('conteudo', 'categoria_nome', 'imagem', 'fonte', 'tags')}),
            ]
        return [
            ('Principais', {'fields':(('publicar',),('titulo','subtitulo'), 'chamada')}),
            ('Principais', {'fields':('conteudo', 'categoria_nome', 'imagem', 'fonte', 'tags')}),

            ]

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            defaults = {}
        else:
            defaults = {'exclude': ('publicar',)}
        defaults.update(kwargs)
        return super(NoticiaAdmin, self).get_form(request, obj, **defaults)
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()


    list_display = ['titulo','destaque', 'publicar', 'categoria_nome', 'criado_em', 'cliques']
    list_filter = ['usuario','categoria_nome', 'publicar', 'destaque']
    readonly_fields = ('usuario',)
    search_fields = ['titulo']
    save_on_top= True
    ordering = ['-criado_em']
    inlines = [EventoAdminInline, VideoNoticiaAdmin, VideoInlineAdmin]
    actions = [noticiadestaque_on, noticiadestaque_off, noticiapublicar_on, noticiapublicar_off]

class LinkInline(admin.TabularInline):
    model = Link
    extra = 3

class DownloadAdmin(admin.ModelAdmin):
    form = BuscarCantorAlbum
    fieldsets = [
        ('Principais', {'fields':('publicar',('titulo'), 'cantor_nome', 'ano',)}),
        ('Sobre o álbum', {'fields':('conteudo', 'imagem')}),
    ]
    inlines = [LinkInline]
    list_display = ['titulo', 'cantor_nome', 'publicar', 'destaque', 'cliques', 'criado_em']
    list_filter = ['cantor_nome', 'publicar', 'destaque', 'cantor_nome__genero_nome', 'ano']
    search_fields = ('cantor_nome__nome', 'titulo')
    save_on_top= True

class GeneroAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principais', {'fields':['nome']}),
    ]

class EventoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'dataevento', 'evento_cidade', 'evento_estado', 'dataevento')
    list_filter = ('local__cidade_uf__uf',)

admin_site.register(Categoria, CategoriaAdmin)
admin_site.register(Noticias, NoticiaAdmin)
admin_site.register(Album, DownloadAdmin)
admin_site.register(Link)
admin_site.register(Eventos, EventoAdmin)