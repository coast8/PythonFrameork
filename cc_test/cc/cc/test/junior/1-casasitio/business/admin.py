# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.contrib import admin

from business.models import Proposta, AndamentoProposta, Visita
from business.forms import AndamentoPropostaForm

class AndamentoAdminInline(admin.TabularInline):
    form = AndamentoPropostaForm
    model = AndamentoProposta
    extra = 1
    fieldsets = [
        ('Observação', {'fields':('observacao',)}),
    ]
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()

class VisitaInline(admin.StackedInline):
    model = Visita
    extra = 0
    fieldsets = [
        ('Horário', {'fields': (('data_visita_ini', 'data_visita_fim'),)}),
        ('Custos', {'fields': ('carro', ('pago', 'gasolina', 'km', 'valor_viagem'),)}),
        ('Descrição', {'fields': ('tipo', 'descricao', 'proposta')}),
    ]
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()

class PropostaAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('cliente', 'n_pessoas', 'get_cliente_identificacao', 'get_proprietario_imovel', 'tipo_evento', 'status', 'prioridade', 'datainicio', 'get_data_proximo_contato', 'usuario_cadastrou')
    list_filter = ('status',)
    readonly_fields = ('criado_em', 'atualizado_em')
    ordering = ('-id',)
    list_per_page = 50
    inlines = (AndamentoAdminInline, VisitaInline)
    related_search_fields = {'cliente': ('nome',),
                             'imovel': ('marca',),}
    fieldsets = [
        ('Cliente', {'fields':('cliente',)}),
        ('Dados Gerais', {'fields':('prioridade', 'status',('n_pessoas', 'tipo_evento'), ('datainicio', 'datafim'),('criado_em', 'atualizado_em'),)}),
        ('Dados da proposta', {'fields':(('dataproximocontato', 'imovel'),)}),
        ('Encerramento da proposta', {
                    'classes': ('collapse',),
                    'fields':('observacao',)}),
    ]
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.usuario = request.user
            instance.usuario_modificado = request.user
            instance.save()
        formset.save_m2m()

    def suit_row_attributes(self, obj):
        class_map = {
            '6': 'success',
            '1': 'warning',
            '5': 'error',
            '2': 'info',
            '3': 'info',
            '4': 'info',
            }
        css_class = class_map.get(obj.status)
        if css_class:
            return {'class': css_class}

class VisitaAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()
    fieldsets = [
        ('Horário', {'fields': (('data_visita_ini', 'data_visita_fim'),)}),
        ('Custos', {'fields': ('carro', ('pago', 'gasolina', 'km', 'valor_viagem'),)}),
        ('Descrição', {'fields': ('tipo', 'descricao', 'proposta')}),
    ]
    list_display = ('__unicode__', 'data_visita_ini', 'carro', 'valor_viagem')

admin.site.register(Visita, VisitaAdmin)
admin.site.register(Proposta, PropostaAdmin)