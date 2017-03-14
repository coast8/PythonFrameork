# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

def marcar_destaque(modeladmin, request, queryset):
    queryset.update(destaque=True)
marcar_destaque.short_description = "Marcar selecionadas como destaque"

def desmarcar_destaque(modeladmin, request, queryset):
    queryset.update(destaque=False)
desmarcar_destaque.short_description = "Desmarcar selecionadas como destaque"