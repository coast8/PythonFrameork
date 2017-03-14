from __future__ import unicode_literals
# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

import datetime
from django.db import models

from contato.models import Pessoa, Lideranca
from core.choices import STATUS_SOLICITACAO, TIPO_CONSULTA

class Assunto(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Assunto'
        verbose_name_plural = 'Assuntos'

class Especialidade(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

class AtendimentoGabinete(models.Model):
    atendido = models.BooleanField('Atendido', default=False)
    pessoa = models.ForeignKey(Pessoa)
    data_chegada = models.DateTimeField('Data de chegada', default=datetime.datetime.now())
    hora_atendimento = models.DateTimeField('Horário de atendimento', blank=True, null=True)
    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
    def __unicode__(self):
        return self.pessoa.nome
    def data_chegada_str(self):
        return self.data_chegada.strftime("%d/%m - %H:%M")
    data_chegada_str.admin_order_field = 'data_chegada'
    data_chegada_str.short_description = 'Horário de chegada'
    def get_telefone_cliente(object):
        if object.pessoa.bairro:
            return object.pessoa.bairro.nome
    get_telefone_cliente.short_description = 'Bairro'
    def save(self, *args, **kwargs):
        if self.atendido == 1:
            self.hora_atendimento = datetime.datetime.now()
        super(AtendimentoGabinete, self).save(*args, **kwargs)
class Solicitacao(models.Model):
    status = models.CharField('Status', max_length=2, choices=STATUS_SOLICITACAO, default='1')
    assunto = models.ForeignKey(Assunto)
    solicitacao = models.TextField('Solicitação', blank=True, null=True)
    resposta = models.TextField('Resposta', blank=True, null=True)
    observacao = models.TextField('Observação', blank=True, null=True)
    pessoa = models.ForeignKey(Pessoa, blank=True, null=True)
    atendimento = models.ForeignKey(AtendimentoGabinete, blank=True, null=True)
    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'

class Consulta(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    tipo = models.CharField('Tipo', max_length=2, choices=TIPO_CONSULTA)
    especialidade = models.ForeignKey(Especialidade)
    lideranca = models.ForeignKey(Lideranca, related_name='lideranca_set')
    data_chegada = models.DateTimeField('Data de chegada', default=datetime.datetime.now())
    data_recebimento = models.DateTimeField('Data de recebimento', blank=True, null=True)
    observacao = models.TextField('Observação', blank=True, null=True)
    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'