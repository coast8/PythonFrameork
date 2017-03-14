# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from models import *
from noticias.models import *
from igenius.models import *
from yawdadmin import admin_site
from igenius.forms import *
from blogs.admin import *
from times.models import *

def publicar(ModelAdmin, request, queryset):
    queryset.update(publicar = True)
publicar.short_description = "Publicar notícia"

def update(ModelAdmin, request, queryset):
    queryset.update(data = datetime.now())

def destaque(ModelAdmin, request, queryset):
    queryset.update(destaque = True)
destaque.short_description = "Marcar notícia como destaque"

def ddestaque(ModelAdmin, request, queryset):
    queryset.update(destaque = False)
ddestaque.short_description = "Desmarcar notícia como destaque"

def extra(ModelAdmin, request, queryset):
    queryset.update(extra = True)
extra.short_description = "Marcar notícia como Extra"

def dextra(ModelAdmin, request, queryset):
    queryset.update(extra = False)
dextra.short_description = "Desmarcar notícia como Extra"

def manchete(ModelAdmin, request, queryset):
    queryset.update(manchete = True)
manchete.short_description = "Marcar notícia como manchete"

def dmanchete(ModelAdmin, request, queryset):
    queryset.update(manchete = False)
dmanchete.short_description = "Desmarcar notícia como manchete"


def despublicar(ModelAdmin, request, queryset):
    queryset.update(publicar = False)
despublicar.short_description = "Despublicar notícia"

class PosicaoAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Cadastrar Posição', {'fields':['nome']}),

        ]
    list_display = ['nome']
    list_filter = ['nome']
    search_fields = ['nome']

class CategoriaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Cadastrar Categoria',{'fields':((('nome','descricao')))}),
    ]
    list_display = ('nome','descricao')
    list_filter = ['nome']
    search_fields = ['nome']
    ordering = ['-nome']

class SubCategoriaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Cadastrar Sub Categoria',{'fields':((('nome','categoria','descricao')))}),
    ]
    list_display = ('nome','categoria')
    list_filter = ['nome']
    search_fields = ['nome']
    ordering = ['-nome']


class AdminNoticia(admin.ModelAdmin):
    class Media:
        js = ("/static/js/jquery-1.9.0.min.js",
              "/static/js/admin/ocultar-admin.js",
        )
    fieldsets = [
        ('Cadastrar Notícia', {'fields':(('publicar','manchete','extra'),('titulo','subtitulo','chamada','subcategoria'),('fonte','link'),('usarVideo','video','tag','autor'),'imagemDestaque')}),
        ('', {'fields':('conteudo',) }),
        ]
    list_display = ['titulo','subcategoria','publicar','manchete','extra','datapublicacao', 'hits']
    list_filter = ['autor', 'manchete','subcategoria','subcategoria__categoria']
    search_fields = ['titulo']
    ordering = ['-datapublicacao']
    form = NoticiaAdd
    affix = False
    actions = [publicar,despublicar,manchete,dmanchete,extra,dextra]

class AdminNoticiaTimes(admin.ModelAdmin):
    class Media:
        js = ("/static/js/jquery-1.9.0.min.js",
              "/static/js/admin/ocultar-admin.js",
        )
    fieldsets = [
        ('Cadastrar Notícia', {'fields':(('publicar','manchete','extra'),('titulo','subtitulo','chamada','subcategoria'),('fonte','link','time','campeonato'),('usarVideo','video','tag','autor'),'imagemDestaque')}),
        ('', {'fields':('conteudo',) }),
        ]
    list_display = ['titulo','subcategoria','publicar','manchete','extra','datapublicacao', 'hits']
    list_filter = ['autor', 'manchete','subcategoria']
    search_fields = ['titulo']
    ordering = ['-datapublicacao']
    form = NoticiaAdd
    affix = False
    actions = [publicar,despublicar,manchete,dmanchete,extra,dextra]

class AdminNoticiaLocal(admin.ModelAdmin):
    class Media:
        js = ("/static/js/jquery-1.9.0.min.js",
              "/static/js/admin/ocultar-admin.js",
        )
    fieldsets = [
        ('Cadastrar Notícia', {'fields':(('publicar','manchete','extra','bairro'),('titulo','subtitulo','chamada','subcategoria'),('fonte','link'),('usarVideo','video','tag','autor'),'imagemDestaque')}),
        ('', {'fields':('conteudo',) }),
        ]
    list_display = ['titulo','subcategoria','publicar','manchete','extra','datapublicacao', 'hits']
    list_filter = ['autor', 'manchete']
    search_fields = ['titulo']
    ordering = ['-datapublicacao']
    form = NoticiaAdd
    affix = False
    actions = [publicar,despublicar,manchete,dmanchete,extra,dextra]


admin.site.register(SubCategoria,SubCategoriaAdmin)
admin.site.register(Fonte)
admin.site.register(Posicao)
admin.site.register(Colaborador)
admin.site.register(CategoriaNoticia,CategoriaAdmin)
admin.site.register(Noticia, AdminNoticia)
admin.site.register(NoticiaTimes, AdminNoticiaTimes)
admin.site.register(Times)
admin.site.register(uf)
admin.site.register(Cidade)
admin.site.register(Bairros)
admin.site.register(Campeonato)
admin.site.register(Local)
admin.site.register(Cores)
admin.site.register(NoticiaLocal,AdminNoticiaLocal)




