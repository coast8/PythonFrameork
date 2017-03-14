# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin
from yawdadmin import admin_site
from models import PubliTexto, PubliImagem


class PublicidadeImagemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principais', {'fields':('ativo', 'nome')}),
        ('Datas', {'fields':(('dataentrada', 'datasaida'), 'empresa_nome')}),
        ('Publicidade', {'fields':('tipo', 'link', 'arquivo')}),
    ]
    list_display = ['nome', 'link', 'tipo', 'dataentrada', 'datasaida', 'ativo',]
    search_fields = ['nome', 'empresa_nome', 'link']
    list_filter = ['tipo']
    ordering = ['-dataentrada']

class PublicidadeTextoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principais', {'fields':('ativo', 'nome')}),
        ('Datas', {'fields':(('dataentrada', 'datasaida'), 'empresa_nome')}),
        ('Publicidade', {'fields':('tipo', 'link', 'texto')}),
    ]
    list_display = ['nome', 'link', 'tipo', 'dataentrada', 'datasaida', 'ativo',]
    search_fields = ['nome', 'empresa_nome', 'link']
    list_filter = ['tipo']
    ordering = ['-dataentrada']

admin_site.register(PubliImagem, PublicidadeImagemAdmin)
admin_site.register(PubliTexto, PublicidadeTextoAdmin)
