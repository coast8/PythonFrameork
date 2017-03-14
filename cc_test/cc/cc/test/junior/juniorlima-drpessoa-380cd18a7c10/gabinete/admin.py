# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.contrib import admin

from gabinete.models import Solicitacao, Pessoa, AnexoSolicitacao, AndamentoSolicitacao, Telefone, Intermediario, Avancado, Atendimento

class AndamentoSolicitacaoInline(admin.TabularInline):
    model = AndamentoSolicitacao
    fields = ('andamento',)
    extra = 1
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificado = request.user
        obj.save()

class AnexoSolicitacaoInline(admin.TabularInline):
    model = AnexoSolicitacao
    extra = 1

class TelefoneInline(admin.TabularInline):
    model = Telefone
    fields = ('tipo', 'telefone',)

class SolicitacaoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Solicitação', {'fields': (('status', 'prioridade', 'tipo'), 'pessoa', 'dataabertura', ('assunto', 'unidade'), 'areadeinteresse', 'encaminhado', 'solicitacao')}),
    )
    inlines = (AndamentoSolicitacaoInline, AnexoSolicitacaoInline)
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificado = request.user
        obj.save()

class PessoaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Principal', {'fields': (('tipo', 'gruposocial', ), 'nome', 'apelido', 'unidadevinculada', ('sexo', 'nascimento'),'foto', 'notas')}),
        ('Dados Adicionais', {
            'classes': ('collapse',),
            'fields': ('site', 'email', 'apelido', 'tratamento', 'empregador')}),
    )
    inlines = (TelefoneInline, )

class AtendimentoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Principal', {'fields': ('dataabertura', ('assunto', 'unidade'), 'pessoa', 'atendimento', ('status', 'prioridade', 'tipo'),)}),
    )

admin.site.register(Solicitacao, SolicitacaoAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Intermediario)
admin.site.register(Avancado)
admin.site.register(Atendimento, AtendimentoAdmin)