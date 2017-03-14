# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.db import models

from core.br_states import STATE_CHOICES

class Logradouros(models.Model):
    endereco= models.CharField('Endereço', max_length=64, blank=True, null=True)
    cep = models.CharField('CEP', max_length=9, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=30, blank=True, null=True)
    cidade = models.CharField('Cidade', default='Teresina',max_length=40, blank=True, null=True)
    uf = models.CharField('UF', default='PI', max_length = 2, choices=STATE_CHOICES)
    class Meta:
        abstract = True