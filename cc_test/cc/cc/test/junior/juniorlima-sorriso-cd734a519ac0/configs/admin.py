# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.contrib import admin

from .models import Configuracao, Habilidade, Servico

class ConfiguracaoAdmin(admin.ModelAdmin):
    pass

class HabilidadeAdmin(admin.ModelAdmin):
    pass

class ServicoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Configuracao, ConfiguracaoAdmin)
admin.site.register(Habilidade, HabilidadeAdmin)
admin.site.register(Servico, ServicoAdmin)