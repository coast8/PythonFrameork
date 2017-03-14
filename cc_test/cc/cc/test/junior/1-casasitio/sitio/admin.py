# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.contrib import admin

from sitio.models import TipoImovel, TipoEvento, TipoOperacao, Estado, Cidade, Zona, Propriedade

class TipoImovelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}

class TipoEventoAdmin(admin.ModelAdmin):
    pass

class TipoOperacaoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}

class EstadoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slugsigla": ("nome",)}

class CidadeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slugcidade": ("nome",)}

class ZonaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Carro', {'fields': ('publicar', ('nome', 'localizacao'),)}),
        ('Informações', {'fields': ('cidade_uf',)})
    ]

class PropriedadeAdmin(admin.ModelAdmin):
    save_on_top = True
    fieldsets = [
        ('Propriedade', {'fields': (('publicar', 'destaque'), 'nome', 'ficticio', 'proprietario', 'resumo_sitio')}),
        ('Disponibilidade', {'fields': (('carnaval', 'semana_santa', 'reveillon', 'outro'),)}),
        ('Dados do Imóvel', {'fields': (('operacao', 'categoria', 'zona'), 'tipoevento',)}),
        ('Informações gerais', {'fields': (('quartos', 'banheiros', 'pessoas', 'capacidadeevento', 'capacidadepernoite'),)}),
        ('Informações Financeiras',
         {
             'description': 'Informe o valor da diária e o percentual de lucro que deseja',
             'fields':((('diaria', 'tipodiaria'), ('negociacao', 'lucro', 'valorfinal'),))}),
        ('Informações detalhadas', {
            'description': 'Marque o que possui na propriedade',
            'fields':(
                ('casa', 'piscinaadulto', 'campodefutebol'),
                ('casasede', 'casaduplex', 'chale', 'murado'),
                ('suite', 'quarto', 'armador', 'mobiliado'),
                ('salaodefesta', 'salaodeculto', 'salasdereunioes',),
                ('som', 'sinuca', 'pingpong', 'dvd', 'tv', 'internet'),
                ('trilha', 'lago', 'cachoeira', 'praia', 'bosque', 'zoologico', 'parque', 'jardim'),
                ('alojamento', 'banheiro', 'vestiariofeminino', 'vestiariomasculino', 'sala', 'bercario', 'capela', 'estacionamento'),
                ('cozinhacomum', 'cozinhaindustrial', 'restaurante', 'alimentacao', 'freezer', 'bar', 'geladeira', 'microondas', 'fogao', 'churrasqueira'),
                ('areadeservico', 'campodevolei', 'campodegolf', 'quadrapoliesportiva', 'quadradetenis', 'piscinainfantil', 'playground', 'cadeirante'),

        )}),
        ('Informação padrão', {'fields': ('descricao',)}),
        ('Informações importantes', {'fields': ('informacao_cliente', 'localizacao')}),
        ('Informações extras', {'fields': ('dados_negociacao', 'dados_especificos')}),
    ]
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        obj.usuario_modificou = request.user
        obj.save()

admin.site.register(TipoImovel, TipoImovelAdmin)
admin.site.register(TipoEvento, TipoEventoAdmin)
admin.site.register(TipoOperacao, TipoOperacaoAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Zona, ZonaAdmin)
admin.site.register(Propriedade, PropriedadeAdmin)