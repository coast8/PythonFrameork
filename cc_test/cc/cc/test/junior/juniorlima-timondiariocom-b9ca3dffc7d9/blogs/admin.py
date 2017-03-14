# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin
from yawdadmin import admin_site
from models import BlogCategoria, Blog, NoticiaBlog, BlogUsuario, NoticiaBlogVideo, PublicidadeBlog
from igenius.forms import *

from publicidades.models import *

def noticianaodestaque(modeladmin, request, queryset):
    queryset.update(destaque=False)
noticianaodestaque.short_description = "Desmarcar notícias como destaque"

def ativar(modeladmin, request, queryset):
    queryset.update(ativo=True)
ativar.short_description = "Ativar Blog"

def desativar(modeladmin, request, queryset):
    queryset.update(ativo=False)
desativar.short_description = "Desativar Blog"

def publicar(modeladmin, request, queryset):
    queryset.update(publicar=True)
publicar.short_description = "Publicar Notícia"

def despublicar(modeladmin, request, queryset):
    queryset.update(destaque=False)
despublicar.short_description = "Despublicar Notícia"

def noticiadestaque(modeladmin, request, queryset):
    queryset.update(destaque=True)
noticiadestaque.short_description = "Marcar notícias como destaque"

class VideodestaqueBlogInlineAdmin(admin.TabularInline):
    fieldsets = [
        ('Extras', {'fields': ('usarVideo', 'video', 'descricaovideo'), 'classes': ['collapse']})
    ]
    model = NoticiaBlogVideo
    extra = 0

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principal', {'fields':((('ativo', 'nome', 'categoria_nome','cor','colaborador'),'email'))}),
        ('Apresentação', {'fields':(('resumo', 'descricao'),())}),
        ('Mídia', {'fields':('imagem_capa', 'imagem_extra')}),

    ]
    ordering = ('-criado_em',)
    list_display = ('nome', 'criado_em', 'ativo', 'cliques')
    list_filter = ('ativo', 'categoria_nome')
    search_fields = ('nome',)
    #readonly_fields = ('usuario',)
    actions = [ativar,desativar]

class PublicidadeBlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principal', {'fields':(('ativo','blog','nome','valor','valorEntrada'),('arquivo','valorFinal'))}),
        ('Datas', {'fields':(('data_entrada', 'data_saida'),())}),

    ]
    ordering = ('-data_entrada',)
    list_display = ('nome', 'blog', 'valor','data_entrada','data_saida','valorFinal','ativo')
    list_filter = ('ativo', 'blog')
    search_fields = ('nome','blog')
    readonly_fields = ('valorFinal',)
    actions = [ativar,desativar]


class BlogUsuarioAdmin(admin.ModelAdmin):
    list_display = ('blog', 'nome_usuario',)
    search_fields = ('blog__nome', 'usuario__username',)

class destaqueBlogAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'blog', 'criado_em', 'publicar', 'destaque', 'cliques')
    list_filter = ['publicar', 'blog']
    search_fields = ['titulo']
    readonly_fields = ('usuario',)
    inlines = [VideodestaqueBlogInlineAdmin]
    actions = [noticiadestaque,noticianaodestaque,publicar,despublicar]
    form = BlogNoticia
    affix = False

    # Salvando o usuário que fez o cadastro
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'colaborador.usuario', None) is None:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()


    # O usuário só ver a notícia que ele cadastrou. O superuser pode visualizar todas
    def queryset(self, request):
        qs = super(destaqueBlogAdmin,self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(blog__usuario=request.user)

    # O usuário não pode colocar destaque na página inicial

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return [
        ('Principais', {'fields':((('publicar','destaque','titulo','subtitulo','blog')),)}),
        ('Conteudo', {'fields':('conteudo','imagem')}),
            ]

        return [
        ('Principais', {'fields':((('publicar','titulo','subtitulo','blog')),)}),
        ('Conteudo', {'fields':('conteudo','imagem')}),
        ]

    # O usuário só pode inserir notícia no blog que ele foi cadastrado
    def get_form(self, request, obj=None, **kwargs):

        self.request = request
        f = super(destaqueBlogAdmin,self).get_form(request, obj)
        return f

    def formfield_for_dbfield(self, dbfield, **kwargs):
        if dbfield.name == 'blog':
            kwargs['queryset'] = BlogUsuario.objects.filter(usuario=self.request.user)
        return super(destaqueBlogAdmin, self).formfield_for_dbfield(dbfield, **kwargs)


admin_site.register(NoticiaBlog, destaqueBlogAdmin)
admin_site.register(BlogUsuario, BlogUsuarioAdmin)
admin_site.register(Blog, BlogAdmin)
admin_site.register(BlogCategoria)
admin_site.register(PublicidadeBlog,PublicidadeBlogAdmin)

