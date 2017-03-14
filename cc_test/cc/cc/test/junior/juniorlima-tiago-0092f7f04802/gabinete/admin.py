# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin

from gabinete.models import Assunto, Especialidade, AtendimentoGabinete, Solicitacao, Consulta

class SolicitacaoInline(admin.StackedInline):
    model = Solicitacao
    extra = 1

class AtendimentoGabineteAdmin(admin.ModelAdmin):
    inlines = (SolicitacaoInline,)
    fieldsets = [
        ('Informações',{'fields':('pessoa', 'data_chegada', ('atendido', 'hora_atendimento'),)}),
    ]

    list_display = ('pessoa', 'get_telefone_cliente', 'data_chegada_str', 'atendido')
    ordering = ('-data_chegada',)
    #list_editable = ['atendido',]

admin.site.register(Assunto)
admin.site.register(Especialidade)
admin.site.register(AtendimentoGabinete, AtendimentoGabineteAdmin)
admin.site.register(Solicitacao)
admin.site.register(Consulta)