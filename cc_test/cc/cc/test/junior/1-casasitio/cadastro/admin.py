# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.contrib import admin

from cadastro.models import PreCliente, Cliente, Proprietario, Carro, TipodeConta

class PreClienteAdmin(admin.ModelAdmin):
    class Media:
        js = (
              "/static/extra-admin/js/nonodig.js",
        )
    fieldsets = [
        ('Cliente', {'fields':(('ativo', 'tipo'), 'nome', ('operadora', 'telefone'),)}),
        ('Informação', {'fields':(('origem', 'identificacao'),)}),
        ('Telefone adicional', {
            'classes': ('collapse',),
            'fields':('operadora_adc', 'telefone_adc',)}),
        ('Endereço', {'fields':(('endereco', 'bairro', 'cep', 'cidade', 'uf'),)}),
        ('Adicional', {'fields':('observacao',)}),
        ('Dados Sociais', {
            'classes': ('collapse',),
            'fields':(('facebook', 'instagram'), 'email',)}
        ),
    ]
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()

class ClienteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Cliente', {'fields':(('ativo', 'tipo'), ('nome', 'nome_completo'), ('operadora', 'telefone'),)}),
        ('Informação', {'fields':(('origem', 'identificacao'),)}),
        ('Documentação', {'fields':(('rg', 'cpf'),('razao_social', 'cnpj'),)}),
        ('Telefone adicional', {
            'classes': ('collapse',),
            'fields':('operadora_adc', 'telefone_adc',)}),
        ('Endereço', {'fields':(('endereco', 'bairro', 'cep', 'cidade', 'uf'),)}),
        ('Adicional', {'fields':('observacao',)}),
        ('Dados Sociais', {
            'classes': ('collapse',),
            'fields':(('facebook', 'instagram'), 'email',)}
        ),
    ]
    class Media:
        js = (
              "/static/extra-admin/js/nonodig.js",
        )
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()
    save_on_top = True

class ProprietarioAdmin(admin.ModelAdmin):
    class Media:
        js = (
              "/static/extra-admin/js/nonodig.js",
        )
    save_on_top = True
    fieldsets = [
        ('Dados Iniciais', {'fields': ('ativo', ('nome', 'apelido'), ('operadora', 'telefone'), ('rg', 'cpf'),)}),
        ('Dados Administrativos', {'fields': (('operadora_adc', 'telefone_adc'), 'caseiro', 'telefone_caseiro')}),
        ('Dados Adicionais', {'fields': ('datanascimento', ('email', 'profissao'),)}),
        ('Logradouro', {'fields':('endereco', 'cep', 'bairro', ('cidade', 'uf')),
                        'classes':('collapse',),
        }),
        ('Extras', {'fields': ('observacoes',)})
    ]

class CarroAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Carro', {'fields': ('ativo', ('modelo', 'dono'),)}),
        ('Informações', {'fields': ('placa', 'cor', 'kmporlitro',)})
    ]

class TipodeContaAdmin(admin.ModelAdmin):
    pass

admin.site.register(PreCliente, PreClienteAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proprietario, ProprietarioAdmin)
admin.site.register(Carro, CarroAdmin)
admin.site.register(TipodeConta, TipodeContaAdmin)