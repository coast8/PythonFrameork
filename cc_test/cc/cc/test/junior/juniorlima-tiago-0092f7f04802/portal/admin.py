# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.contrib import admin

from .models import Postagem, Categoria

class CategoriaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Categoria', {'fields': ('publicar', 'nome', 'descricao',)}),
    )
    list_display = ('publicar', 'nome', 'descricao')

class PostagemAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Publicação', {'fields': (('publicar', 'destaque'), 'titulo', 'subtitulo', 'conteudo',)}),
        ('Classificação', {'fields': ('categoria', ('imagem', 'imagem_disco'),'data_publicacao',)}),
    )
    list_display = ('titulo', 'categoria', 'publicar', 'destaque')
    list_filter = ('categoria',)
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Postagem, PostagemAdmin)
