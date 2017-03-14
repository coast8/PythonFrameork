# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

from core.choices import OPERADORA_CHOICES, ORIGEM_CHOICES

class Usuario(models.Model):
    user = models.OneToOneField(User)
    # Dados Adicionais
    operadora = models.CharField('Operadora', max_length=2, choices=OPERADORA_CHOICES, default='1')
    origem = models.CharField('Origem', max_length=2, choices=ORIGEM_CHOICES, default=2)
    telefone = models.CharField('Telefone', max_length=15, blank=True, null=True)
    telefone_add = models.CharField('Telefone Adicional', max_length=15, blank=True, null=True)
    data_nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    facebook = models.CharField('Facebook', max_length=30,blank=True, null=True)
    instagram = models.CharField('Instagram', max_length=30,blank=True, null=True)
    observacao = models.TextField('Observação', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
