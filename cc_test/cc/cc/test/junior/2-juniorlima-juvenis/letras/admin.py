# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin
from yawdadmin import admin_site
from letras.models import Genero, Cantor, Letra
from forms import BuscarAlbumAdminForm
class GeneroAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Mídia', {'fields':('ativo', 'nome')}),
    ]
    list_display = ('nome', 'ativo', 'cliques')
    list_filter = ('ativo',)
    search_fields = ('nome',)

class CantorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informação', {'fields':(('publicar', 'destaque', 'inicial'), 'nome',)}),
        ('Caracteristicas', {'fields':('genero_nome', 'siteoficial')}),
        ('Descrição', {'fields':('descricao',)}),
        ('Mídia', {'fields':(('foto01', 'foto02', 'foto03'),)}),
    ]
    list_display = ('nome', 'publicar', 'destaque', 'inicial', 'genero_nome', 'cliques')
    list_filter = ('publicar', 'destaque', 'genero_nome')
    search_fields = ('nome',)

class LetraAdmin(admin.ModelAdmin):
    form = BuscarAlbumAdminForm
    fieldsets = [
        ('Principais', {'fields':(('publicar','destaque'),('titulo'),)}),
        ('Conteudo', {'fields':('album_nome', 'conteudo', 'urlvideo')}),
        ('Outras informações', {'fields': ('usuario','slug'),'classes': ('collapse',)})
    ]
    list_display = ('titulo', 'album_nome', 'publicar', 'destaque', 'cliques')
    list_filter = ('publicar', 'destaque', 'album_nome', 'album_nome__cantor_nome')
    search_fields = ('titulo',)
    save_on_top = True
    readonly_fields = ('usuario', 'slug')

admin_site.register(Genero, GeneroAdmin)
admin_site.register(Cantor, CantorAdmin)
admin_site.register(Letra, LetraAdmin)