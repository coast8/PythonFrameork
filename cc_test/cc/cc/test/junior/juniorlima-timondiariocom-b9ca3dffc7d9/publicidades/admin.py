# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin
from yawdadmin import admin_site
from models import Publicidade


class publicidadeAdmin(admin.ModelAdmin):
    class Media:
        js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
    fieldsets = [
        ('Principais', {'fields':(('ativo','patrocinado','tipo','nome'))}),
        ('Configurações de Data', {'fields':(('data_entrada','data_saida'))}),
        ('Conteudo', {'fields':('arquivo','url','adsense')}),
        ]
    list_display = ['nome', 'tipo','url','data_entrada','data_saida','ativo']
    list_filter = ['nome']
    search_fields = ['nome']
    save_on_top= True
    ordering = ['data_entrada']


admin_site.register(Publicidade, publicidadeAdmin)
