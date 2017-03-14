# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

def publicar_site(modeladmin, request, queryset):
    queryset.update(publicar=True)
publicar_site.short_description = "Publicar do site"

def despublicar_site(modeladmin, request, queryset):
    queryset.update(publicar=False)
despublicar_site.short_description = "Despublicar do site"

def destaque_site(modeladmin, request, queryset):
    queryset.update(destaque=True)
destaque_site.short_description = "DESTACAR - ADD"

def del_destaque_site(modeladmin, request, queryset):
    queryset.update(destaque=False)
del_destaque_site.short_description = "DESTACAR - DEL"