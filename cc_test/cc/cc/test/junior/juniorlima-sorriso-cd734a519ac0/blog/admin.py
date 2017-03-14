# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.contrib import admin

from blog.models import Postagem, Categoria

def make_destaque(modeladmin, request, queryset):
    queryset.update(destaque=True)
make_destaque.short_description = "Marcar como destaque"

def desmake_destaque(modeladmin, request, queryset):
    queryset.update(destaque=False)
desmake_destaque.short_description = "Desmarcar como destaque"


class PostagemAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Publicação', {'fields': (('publicar', 'destaque'), 'titulo', 'subtitulo', 'conteudo',)}),
        ('Classificação', {'fields': ('categoria', ('imagem'),)}),
    )
    list_display = ('titulo', 'categoria', 'data_publicacao', 'cliques','publicar', 'destaque')
    list_filter = ('categoria', 'destaque', 'destaque')
    actions = (make_destaque, desmake_destaque)
    save_on_top = True
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()



admin.site.register(Categoria)
admin.site.register(Postagem, PostagemAdmin)