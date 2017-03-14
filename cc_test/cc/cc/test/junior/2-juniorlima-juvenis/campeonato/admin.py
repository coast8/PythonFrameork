# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin
from yawdadmin import admin_site
from models import *
from forms import TimeForm, JogadorForm

class CampeonatoAdmin(admin.ModelAdmin):
    pass

class JogadorInline(admin.TabularInline):
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.usuario = request.user
        obj.last_modified_by = request.user
        obj.save()
    def queryset(self, request):
        buscauser = super(JogadorInline, self).queryset(request)
        if request.user.is_superuser:
            return buscauser
        return buscauser.filter(usuario=request.user)
    fieldsets = [
        ('Jogador', {'fields':(('nome', 'datanascimento', 'rg'),)}),
        ('Dados', {'fields':(('telefone', 'facebook', 'foto'),)})
    ]
    model = Jogador
    extra = 8
    max_num = 12
    form = JogadorForm
	
class TimeAdmin(admin.ModelAdmin):
    class Media:
        js = ("/media/jsmask/jquery-1.8.0.js","/media/jsmask/jquery.meio.mask.js","/media/jsmask/tools.js")

    form = TimeForm
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.usuario = request.user
        obj.last_modified_by = request.user
        obj.save()
    def queryset(self, request):
        buscauser = super(TimeAdmin, self).queryset(request)
        if request.user.is_superuser:
            return buscauser
        return buscauser.filter(usuario=request.user)
    fieldsets = [
        ('Time', {'fields':(('nome', 'bairro', 'igreja'),'campeonato_nome')}),
        ('Perguntas', {'fields':(('jogadorfora', 'quadra'),)}),
        ('Contato', {'fields':('responsavel', ('telefoneresponsavel', 'emailresponsavel', 'facebookresponsavel'),)}),
        ('Técnico', {'fields':(('tecnico', 'telefonetecnico'),)})
    ]
    list_display = ['nome', 'igreja', 'bairro', 'responsavel', 'telefoneresponsavel']
    inlines = [JogadorInline]

class JogadorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Time', {'fields':('escalado', ('nome'), ('datanascimento', 'rg', 'numero'), 'time_nome')}),
        ('Contato', {'fields':(('telefone', 'facebook'), 'foto',)})
    ]
    list_display = ['nome', 'telefone', 'time_nome', 'foto_jogador']
    list_filter = ['time_nome']
    search_fields = ['nome']

    def foto_jogador(self, obj):
        if obj.foto:
            return u'<img src=%s>' % (obj.foto.url_120x90)
        else:
            return u'<img src=/media/img/avatar.png>'
    foto_jogador.short_description = 'Foto'
    foto_jogador.allow_tags = True
	
admin_site.register(Campeonato, CampeonatoAdmin)
admin_site.register(Time, TimeAdmin)
admin_site.register(Jogador, JogadorAdmin)