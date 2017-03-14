# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin

from votacao.models import Voto

class VotoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações',{'fields':('nome_indicacao', 'telefone', ('titulo', 'zona', 'secao'),)}),
    ]
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()

admin.site.register(Voto, VotoAdmin)
