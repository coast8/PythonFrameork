# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.db import models

class Configuracao(models.Model):
    resumo_inicial = models.CharField('Resumo inicial', max_length=250, help_text='Texto de chamada do site')
    historia = models.CharField('História', max_length=250, help_text='Texto sobre carreira')
    def __unicode__(self):
        return 'Resumo e historia de Wellington Sousa'
    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'

class Habilidade(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    nome = models.CharField('Habilidade', max_length=50, unique=True)
    percentagem = models.PositiveSmallIntegerField('Porcentagem', help_text='Insira de 0 a 100')
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'


class Servico(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    nome = models.CharField('Habilidade', max_length=50, unique=True)
    explicacao = models.CharField('Explicação', max_length=100)
    classe_icon = models.CharField('Classe do ícone', max_length=30, help_text='Lista de ícones disponível em: <a href="http://themes-lab.com/make-frontend/pages/elements/icons.html">aqui</a>')
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
