# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin

from ads.models import PubliTexto, PubliImagem, Empresa, Posicao, Formato, Local


class PublicidadeImagemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principais', {'fields':('ativo', 'nome')}),
        ('Datas', {'fields':(('dataentrada', 'datasaida'), 'empresa_nome')}),
        ('Publicidade', {'fields':('posicao', 'link', 'tipo', 'arquivo')}),
    ]
    list_display = ['nome', 'link', 'dataentrada', 'datasaida', 'ativo',]
    search_fields = ['nome', 'empresa_nome', 'link']
    list_filter = ['posicao']
    ordering = ['-dataentrada']

class PublicidadeTextoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principais', {'fields':('ativo', 'nome')}),
        ('Datas', {'fields':(('dataentrada', 'datasaida'), 'empresa_nome')}),
        ('Publicidade', {'fields':('posicao', 'link', 'texto')}),
    ]
    list_display = ['nome', 'link', 'dataentrada', 'datasaida', 'ativo',]
    search_fields = ['nome', 'empresa_nome', 'link']
    list_filter = ['posicao']
    ordering = ['-dataentrada']

admin.site.register(PubliImagem, PublicidadeImagemAdmin)
admin.site.register(PubliTexto, PublicidadeTextoAdmin)
admin.site.register(Empresa)
admin.site.register(Posicao)
admin.site.register(Formato)
admin.site.register(Local)