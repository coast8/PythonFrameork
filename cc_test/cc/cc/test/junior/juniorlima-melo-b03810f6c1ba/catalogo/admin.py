# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'
from django.contrib import admin

from catalogo.models import Categoria, Marca, Produto

class CategoriaAdmin(admin.ModelAdmin):
    pass

class MarcaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações', {'fields': ('nome', 'informacoes',)}),
        ('Informações', {'fields': ('documento',)}),
    ]

class ProdutoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações', {'fields': ('nome', ('marca', 'categoria'),)}),
        ('Informações', {'fields': ('informacoes', 'imagem')}),
    ]
    list_display = ('nome', 'marca', 'categoria')
    list_filter = ('marca', 'categoria')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Produto, ProdutoAdmin)
