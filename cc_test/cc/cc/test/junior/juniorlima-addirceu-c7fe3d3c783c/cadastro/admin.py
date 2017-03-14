# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin

from cadastro.models import Cadastro, Cargo, Congregacao, Funcao, Profissao, Membro, Departamento
from cadastro.forms import MembroForm
from cadastro.filter import AniversarianteMesFilter

class CargoInline(admin.StackedInline):
    model = Cargo
    extra = 1

class MembroAdmin(admin.ModelAdmin):
    def queryset(self, request):
        return self.model.objects.filter(ativo=True)
    list_filter = (AniversarianteMesFilter, 'obreiro', 'ativo')
    list_display = ('nome', 'data_nascimento', 'telefone')
    form = MembroForm
    class Media:
        js = (
              "/static/extra-admin/js/nonodig.js",
        )
    fieldsets = [
        ('Principal', {'fields':(('ativo', 'obreiro'), 'nome', ('sexo', 'estado_civil'), 'data_nascimento', 'telefone')}),
        ('Adicionais', {'fields':('telefone_adc', 'profissao', 'escolaridae', 'email', 'titulo_eleitor')}),
        ('Parentesco', {'fields':('pai', 'mae', )}),
        ('Datas importantes', {'fields':('data_espirito', 'data_aguas')}),
        ('Documentação', {'fields':('cpf', 'rg', 'orgao_expedidor', 'ug_orgao')}),

    ]
    inlines = (CargoInline,)
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()

class CargoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'funcao', 'data_inicial', 'ativo')
    list_filter = ('funcao', 'ativo')

admin.site.register(Cadastro)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Congregacao)
admin.site.register(Funcao)
admin.site.register(Profissao)
admin.site.register(Departamento)
admin.site.register(Membro, MembroAdmin)
