# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.contrib import admin

from portal.models import Postagem, Categoria, VideoPostagem

def make_destaque(modeladmin, request, queryset):
    queryset.update(destaque=True)
make_destaque.short_description = "Marcar como destaque"

def desmake_destaque(modeladmin, request, queryset):
    queryset.update(destaque=False)
desmake_destaque.short_description = "Desmarcar como destaque"


class VideoPostagemInline(admin.StackedInline):
    model = VideoPostagem
    extra = 1

class PostagemAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Publicação', {'fields': (('publicar', 'destaque'), 'chamada', 'titulo', 'subtitulo', 'conteudo',)}),
        ('Classificação', {'fields': ('categoria', ('posicao_foto', 'imagem'), 'data_publicacao')}),
    )
    list_display = ('titulo', 'categoria', 'publicar', 'destaque')
    list_filter = ('categoria', 'destaque')
    save_on_top = True
    inlines = (VideoPostagemInline,)
    actions = (make_destaque, desmake_destaque)
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()


class VideoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Classificação', {'fields': ('url', 'comentario')}),
    )
class FraseAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Classificação', {'fields': ('publicar', 'frase')}),
    )

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'color')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(VideoPostagem)
admin.site.register(Postagem, PostagemAdmin)