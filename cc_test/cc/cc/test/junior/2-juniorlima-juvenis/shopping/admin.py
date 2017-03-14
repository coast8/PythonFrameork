# -*- coding: utf-8 -*-

__author__ = 'Junior Lima'

from django.contrib import admin
from yawdadmin import admin_site
from shopping.models import CategoriaProduto, Marca, Produto

class CategoriaprodutoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações',{'fields':('nome','descricao')}),
    ]
    list_display = ['nome','descricao']

class ProdutoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados do Produto', {'fields':(('titulo',), 'conteudo')}),
        ('Dados do Produto', {'fields':(('categoria_nome', 'loja_nome', 'marca_nome'),('status_ch', 'situacao_ch'),)}),
        ('Dados do Produto', {'fields':(('preconormal', 'desconto', 'precofinal'),)}),
        ('Mídia', {'fields':('fotoum', 'fotodois', 'fototres')}),
    ]
    list_display = ['titulo','categoria_nome', 'loja_nome', 'precofinal', 'status_ch']

admin_site.register(Produto, ProdutoAdmin)
admin_site.register(Marca)
admin_site.register(CategoriaProduto, CategoriaprodutoAdmin)