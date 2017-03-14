# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin
from yawdadmin import admin_site
from models import Cidade, Local, CategoriaLocal, LocalEvento, LogradourosLocal, Estado

class CidadeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principais', {'fields':('nome',)}),
        ('Estado', {'fields':('uf',)}),
    ]

class CategoriaLocalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principais', {'fields':('nome',)}),
    ]

class LocalAdmin(admin.ModelAdmin):
    class Media:
        js = ("/static/yawd-admin/js/jquery.min.js",
              "/static/administrador/js/jquery.maskedinput.min.js",
              "/static/administrador/js/mascara.js",
        )
    fieldsets = [
        ('Principais', {'fields':('nome', 'site', ('imagem'), 'categoria_nome')}),
        ('Localização', {'fields':('lat_long',)}),
        ('Logradouro', {'fields':('endereco',('bairro', 'cep', 'cidade_uf'), ('telefone',))}),
        ('Conteúdo', {'fields':('conteudo',)}),
    ]
    search_fields = ('nome',)
    list_display = ('nome', 'categoria_nome', 'cidade_uf', 'cliques')
    list_filter = ('categoria_nome', 'cidade_uf')


class LocalEventoAdmin(LocalAdmin):
    pass

admin_site.register(Cidade, CidadeAdmin)
admin_site.register(CategoriaLocal, CategoriaLocalAdmin)
admin_site.register(Local, LocalAdmin)
admin_site.register(LogradourosLocal)
admin_site.register(LocalEvento, LocalEventoAdmin)
