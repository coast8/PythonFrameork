# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.contrib import admin

from locacao.models import Fechamento, Pagamento, Documento

class PagamentoInline(admin.StackedInline):
    model = Pagamento
    extra = 0
    fieldsets = [
        ('Pagamento', {'fields': ('recebido', 'tipo_recebimento', 'tipo_receita',('valor', 'lucro', 'repasse'),)}),
        ('Recebimento', {'fields': (('prazo_recebimento', 'data_recebimento'), ('recebimento', 'pagante'),)}),
        ('Repasse', {'fields': ('data_entrega', 'entregue',)}),
    ]

class FechamentoAdmin(admin.ModelAdmin):
    save_on_top = True
    fieldsets = [
        ('Dados do fechamento', {'fields': ('proposta', ('datainicio', 'datafim'),)}),
        ('Dados financeiros', {'fields': (('valorfechado', 'valor_proprietario', 'lucro'),)}),
        ('Detalhes da negociação', {'fields': (('dados_contrato', 'observacao',),)}),
    ]
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()
    ordering = ('-criado_em',)
    list_display = ('__unicode__', 'data_fechamento_in', 'data_inicio_in')
    inlines = (PagamentoInline, )

class PagamentoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados do fechamento', {'fields': ('recebido', 'fechamento', ('tipo_receita', 'tipo_recebimento'),)}),
        ('Dados financeiros', {'fields': (('valor', 'repasse', 'lucro'),)}),
        ('Detalhes da negociação', {'fields': (('prazo_recebimento', 'data_recebimento',), 'recebimento', 'pagante')}),
        ('Detalhes da negociação', {'fields': (('data_entrega', 'entregue',),)}),
        ('Detalhes da negociação', {'fields': ('observacao',)}),
    ]
    ordering = ('-prazo_recebimento',)
    list_display = ('__unicode__', 'prazo_recebimento', 'recebido')
    list_filter = ('fechamento__proposta__imovel__nome',)
    save_on_top = True
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()

admin.site.register(Fechamento, FechamentoAdmin)
admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Documento)
