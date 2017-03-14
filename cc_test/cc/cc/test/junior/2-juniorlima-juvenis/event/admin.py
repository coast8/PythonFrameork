# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin
from event.models import Evento, FotoCapa, Programacao, DiasdePalestra, Ministrante, TipoEvento, GaleriaEvento, Image, Patrocinio, Duvida, Testemunhal, Pessoa, Noticia, Ingresso, Inscricao

class DiasdePalestraAdmin(admin.ModelAdmin):
    pass

class MinistranteAdmin(admin.ModelAdmin):
    pass

class FotoCapaInline(admin.TabularInline):
    model = FotoCapa
    extra = 1

class ProgramacaoInline(admin.StackedInline):
    model = Programacao
    extra = 1

class PatrocinioInline(admin.TabularInline):
    model = Patrocinio
    extra = 4

class DuvidaInline(admin.StackedInline):
    model = Duvida
    extra = 3

class TestemunhalInline(admin.StackedInline):
    model = Testemunhal
    extra = 1

class NoticiaInline(admin.StackedInline):
    model = Noticia
    extra = 2

class EventoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principais', {'fields':('publicar', 'nome', 'data_evento', ('chamada', 'descricao'), ('telefone', 'email'), )}),
        ('Redes Sociais', {'fields':(('facebook', 'twitter', 'plus'),('youtube', 'instagram', 'pinterest', 'linkedid'),)}),
    ]
    inlines = (FotoCapaInline, ProgramacaoInline, PatrocinioInline, DuvidaInline, TestemunhalInline, NoticiaInline)
    list_display = ('nome', 'data_evento')
    #list_filter = ('data_evento',)
    #actions = (propriedade_destaque_add, propriedade_destaque_del, disponivel_carnaval, disponivel_semana_santa, disponivel_reveillon)
    #list_editable = ('publicar', 'destaque')
    #ordering = ('-criado_em',)
    save_on_top = True

class IngressoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'evento')

admin.site.register(Evento, EventoAdmin)
admin.site.register(DiasdePalestra, DiasdePalestraAdmin)
admin.site.register(Ministrante, MinistranteAdmin)
admin.site.register(TipoEvento)
admin.site.register(Programacao)
admin.site.register(GaleriaEvento)
admin.site.register(Image)
admin.site.register(Pessoa)
admin.site.register(Inscricao)
admin.site.register(Ingresso, IngressoAdmin)