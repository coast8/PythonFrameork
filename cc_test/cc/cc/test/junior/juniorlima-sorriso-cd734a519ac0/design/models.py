# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

import datetime
from django.utils import timezone
from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor.fields import RichTextField

from design.choices import PAGAMENTO_TIPO

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50, unique=True)
    tel_pri = models.CharField('Telefone', max_length=15)
    tel_adc = models.CharField('Telefone Adicional', max_length=15, blank=True, null=True)
    email = models.CharField('Email', max_length=70, blank=True, null=True)
    def __unicode__(self):
        return self.nome

class Tipo(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    nome = models.CharField('Nome', max_length=30, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    def __unicode__(self):
        return self.nome
    @models.permalink
    def get_absolute_url(self):
        return ('tipo-list', (), {'slug': self.slug})
        # http://stackoverflow.com/questions/14170473/get-absolute-url-in-django-when-using-class-based-views

class Portifolio(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    destaque = models.BooleanField('Destaque', default=False)
    nome = models.CharField('Nome', max_length=50)
    conteudo = RichTextField('Conteúdo', config_name='juniorlima')
    arte = ThumbnailerImageField('Arte', upload_to='arte', blank=True)
    tipo = models.ForeignKey(Tipo)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    class Meta(object):
        ordering = ('my_order',)
    def __unicode__(self):
        return self.nome
    @models.permalink
    def get_absolute_url(self):
        return ('todos-list', (), {'slug': self.slug})


class Pagamento(models.Model):
    # Pagamento
    pago = models.BooleanField('Pago', default=False)
    tipo_recebimento = models.CharField('Tipo de pagamento', max_length=2, choices=PAGAMENTO_TIPO)
    valor = models.DecimalField('Valor de pagamento', max_digits=10, decimal_places=2)
    portifolio = models.ForeignKey(Portifolio)
    data_entrega = models.DateField('Data de entrega da arte', default=timezone.now)
    # Recebimento
    prazo_pagamento = models.DateField('Prazo para pagamento', default=timezone.now)
    data_pagamento = models.DateField('Data do pagamento', blank=True, null=True)

    observacao = RichTextField('Observação', blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s - %s" % (self.portifolio.cliente.nome, self.prazo_pagamento)

