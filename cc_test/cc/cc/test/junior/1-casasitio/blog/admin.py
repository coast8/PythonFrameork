# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin

from blog.models import Noticia


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicar')
    fieldsets = [
        ('Notícia', {'fields': (('publicar', 'destaque'), 'titulo', 'subtitulo', 'conteudo',)}),
        ('Informações adicionais', {'fields': ('fonte', 'imagem')}),
    ]
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()

admin.site.register(Noticia, NoticiaAdmin)
