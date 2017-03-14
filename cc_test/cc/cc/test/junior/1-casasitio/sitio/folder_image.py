# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from datetime import date

def destino_imagem_propriedade(instance, filename):
    d = date.today()
    ano = d.year
    return '/'.join(['propriedade', str(ano), str(instance.imovel.categoria.slug), str(instance.imovel.slug), filename])

def destino_foto_propriedade(instance, filename):
    d = date.today()
    ano = d.year
    return '/'.join(['propriedade', str(ano), str(instance.categoria.slug), str(instance.slug), 'capa',filename])
