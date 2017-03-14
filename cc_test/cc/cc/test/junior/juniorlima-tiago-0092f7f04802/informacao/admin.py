# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin

from informacao.models import Visita, Participantes

class ParticipanteInline(admin.TabularInline):
    class Media:
        js = (
              "/static/extra-admin/js/nonodig.js",
        )
    fieldsets = [
        ('Informações',{'fields':('nome', 'telefone', )}),
    ]
    model = Participantes
    extra = 10

class VisitaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Visita',{'fields':(('bairro', 'data_visita'), 'endereco', 'acompanhantes', 'lideranca')}),
    ]
    inlines = (ParticipanteInline,)

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'visita')
    list_filter = ('visita',)
admin.site.register(Visita, VisitaAdmin)
admin.site.register(Participantes, ParticipanteAdmin)


