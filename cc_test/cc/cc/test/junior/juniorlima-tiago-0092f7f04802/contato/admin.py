# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin
from contato.models import Lideranca, Pessoa, Coordenadoria, Coordenacao, Zona, Bairro

class PessoaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações',{'fields':('nome', 'telefone', 'endereco', 'bairro', )}),
        ('Dados Adicionais',{'fields':('telefone_adc', 'data_nascimento')}),
    ]
    list_display = ('nome', 'telefone', 'bairro')
    search_fields = ('nome', 'telefone', 'telefone_adc')
    class Media:
        js = (
              "/static/extra-admin/js/nonodig.js",
        )


class CoordenacaoAdmin(admin.ModelAdmin):
    class Media:
        js = (
              "/static/extra-admin/js/nonodig.js",
        )

admin.site.register(Lideranca)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Coordenacao, CoordenacaoAdmin)
admin.site.register(Coordenadoria)
admin.site.register(Zona)
admin.site.register(Bairro)

