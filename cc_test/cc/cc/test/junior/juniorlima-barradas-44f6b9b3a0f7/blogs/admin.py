# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin
from blogs.models import Blog, NoticiaBlog, BlogUsuario


def noticiadestaque(modeladmin, request, queryset):
    queryset.update(destaque=False)
noticiadestaque.short_description = "Desmarcar notícias como destaque"

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principal', {'fields':('ativo', 'nome', 'color', ('igreja', 'email'))}),
        ('Apresentação', {'fields':('resumo', 'descricao')}),
        ('Mídia', {'fields':('imagem_capa', 'imagem_extra')}),

    ]
    ordering = ('-criado_em',)
    list_display = ('nome', 'criado_em', 'ativo', 'color', 'cliques')
    list_filter = ('ativo', )
    search_fields = ('nome',)
    readonly_fields = ('usuario',)
    save_on_top = True

class BlogUsuarioAdmin(admin.ModelAdmin):
    list_display = ('blog', 'nome_usuario',)
    search_fields = ('blog__nome', 'usuario__username',)

class NoticiaBlogAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'blog', 'data_publicacao', 'publicar', 'destaque', 'cliques')
    list_filter = ['publicar', 'blog']
    search_fields = ['titulo']
    readonly_fields = ('usuario',)
    save_on_top= True
    actions = [noticiadestaque]
    # Salvando o usuário que fez o cadastro
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()
    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return [
        ('Principais', {'fields':(('publicar','destaque'),('titulo'),'subtitulo',)}),
        ('Conteudo', {'fields':('conteudo', 'blog','imagem', 'data_publicacao')}),
            ]
        return [
        ('Principais', {'fields':(('publicar',),('titulo'),'subtitulo',)}),
        ('Conteudo', {'fields':('conteudo', 'blog','imagem', 'data_publicacao')}),
        ]
    # O usuário só pode inserir notícia no blog que ele foi cadastrado
    def get_form(self, request, obj=None, **kwargs):
        self.request = request
        f = super(NoticiaBlogAdmin,self).get_form(request, obj)
        return f

admin.site.register(NoticiaBlog, NoticiaBlogAdmin)
admin.site.register(BlogUsuario, BlogUsuarioAdmin)
admin.site.register(Blog, BlogAdmin)