from __future__ import unicode_literals
# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.db import models

class Zona(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zona'

class Bairro(models.Model):
    nome = models.CharField(max_length=70, unique=True)
    zona = models.ForeignKey(Zona)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100, unique=True)
    telefone = models.CharField('Telefone', max_length=15, default='869')
    telefone_adc = models.CharField('Telefone', max_length=15, blank=True, null=True)
    data_nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=100, blank=True, null=True)
    bairro = models.ForeignKey(Bairro, blank=True, null=True)
    def __unicode__(self):
        return self.nome

class Lideranca(Pessoa):
    pass
    class Meta:
        verbose_name = 'Liderança'
        verbose_name_plural = 'Lideranças'

class Coordenadoria(models.Model):
    nome = models.CharField('Nome', max_length=100, unique=True)
    atribuicao = models.TextField('Atribuição', blank=True, null=True)
    class Meta:
        verbose_name = 'Coordernadoria'
        verbose_name_plural = 'Coordenadorias'
    def __unicode__(self):
        return self.nome

class Coordenacao(models.Model):
    nome = models.CharField('Nome', max_length=100, unique=True)
    telefone = models.CharField('Telefone', max_length=15)
    telefone_adc = models.CharField('Telefone', max_length=15, blank=True, null=True)
    cooordenadoria = models.ForeignKey(Coordenadoria)
    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
    def __unicode__(self):
        return self.nome