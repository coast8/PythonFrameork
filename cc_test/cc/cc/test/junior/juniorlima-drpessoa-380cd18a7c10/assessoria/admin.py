# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.contrib import admin

from .models import Postagem, VideoPostagem, Categoria, Institucional, Evento
from assessoria.actions import marcar_destaque, desmarcar_destaque


class CategoriaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Categoria', {'fields': ('publicar', 'nome', 'descricao',)}),
    )
    list_display = ('publicar', 'nome', 'descricao')

class VideoPostagemInline(admin.TabularInline):
    model = VideoPostagem
    extra = 1

class EventoInline(admin.TabularInline):
    model = Evento
    max_num = 1

class PostagemAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Publicação', {'fields': (('publicar', 'destaque'), 'titulo', 'subtitulo', 'conteudo',)}),
        ('Classificação', {'fields': ('categoria', ('imagem'),'data_publicacao',)}),
    )
    list_display = ('titulo', 'categoria', 'publicar', 'destaque')
    list_filter = ('categoria',)
    inlines = (VideoPostagemInline, EventoInline)
    actions = (marcar_destaque, desmarcar_destaque)
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()

class InstitucionalAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Categoria', {'fields': ('perfil',)}),
    )
    list_display = ('perfil',)



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Postagem, PostagemAdmin)
admin.site.register(Institucional, InstitucionalAdmin)
