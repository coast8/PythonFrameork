# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

import datetime, math

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField

from core.choices import BUSINESS_PROPOSTA_PRIORIDADE, BUSINESS_STATUS_PROPOSTA, TIPO_VISITA, BUSINESS_ANDAMENTO_TIPO
from cadastro.models import PreCliente, Carro
from sitio.models import Propriedade, TipoEvento

class Proposta(models.Model):
    imovel = models.ForeignKey(Propriedade, blank=True, null=True)
    cliente = models.ForeignKey(PreCliente)
    prioridade = models.CharField('Prioridade', max_length=2, choices=BUSINESS_PROPOSTA_PRIORIDADE, default='5')
    n_pessoas = models.PositiveSmallIntegerField('Pessoas')
    tipo_evento = models.ForeignKey(TipoEvento, default=1)
    dataproximocontato = models.DateTimeField('Próximo contato', default=datetime.datetime.today()+datetime.timedelta(days=7))
    datainicio = models.DateField('Início')
    datafim = models.DateField('Data de partida', blank=True, null=True)

    status = models.CharField('Status', max_length=2, choices=BUSINESS_STATUS_PROPOSTA, default=1)
    observacao = RichTextField('Descrição Final', blank=True, null=True, config_name='awesome_ckeditor')
    # https://gist.github.com/eduardo-matos/8651166
    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True, editable=False)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    class Meta:
        pass
    def __unicode__(self):
        return "Proposta %d - %s" % (self.id, self.cliente.nome)
    def get_telefone_cliente(object):
        return "%s - %s" % (object.cliente.get_operadora_display(), object.cliente.telefone)
    get_telefone_cliente.short_description = 'Telefone'
    def get_cliente_identificacao(object):
        if object.cliente.identificacao:
            return object.cliente.identificacao
        return 'Não identificado'
    get_cliente_identificacao.short_description = 'Identificação do cliente'
    def get_data_proximo_contato(object):
        if object.dataproximocontato:
            return object.dataproximocontato.strftime('%d/%m/%Y')
    get_data_proximo_contato.short_description = 'Próximo contato'
    get_data_proximo_contato.admin_order_field = 'dataproximocontato'
    def get_proprietario_imovel(object):
        if object.imovel:
            return '%s - %s - %s - %s' % (object.imovel.nome, object.imovel.proprietario.nome, object.imovel.proprietario.get_operadora_display(), object.imovel.proprietario.telefone)
        return 'Procurando imóvel'
    get_proprietario_imovel.short_description = 'Imóvel'
    def usuario_cadastrou(self):
        if self.usuario:
            return self.usuario.first_name
    usuario_cadastrou.short_description = 'Captado por'
    def clean(self):
        if not self.prioridade == '5' and self.status == '1':
            raise ValidationError('Altere o status da negociação')
        if (self.status == '5' or self.status == '7') and not self.observacao:
            raise ValidationError('Descreva como a negociação se encerrou.')
        if self.datafim and self.datainicio:
            if self.datafim < self.datainicio:
                raise ValidationError('A data de fim não pode ser maior do que a de início')
    def save(self, *args, **kwargs):
        if not self.id:
            if self.status == '1':
                self.prioridade = '5'
        super(Proposta, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('sitio.views.proposta', kwargs={'proposta_id': self.id,
                                                      'cliente_id': self.cliente.id,
                                                      })
    def get_absolute_txt(self):
        return reverse('rest.views.proposta-simples', kwargs={'proposta_id': self.id,
                                                      'cliente_id': self.cliente.id,
                                                      })

class AndamentoProposta(models.Model):
    ativo = models.BooleanField(default=True)
    proposta = models.ForeignKey(Proposta)
    tipo = models.CharField('Tipo de proposta', max_length=2, choices=BUSINESS_ANDAMENTO_TIPO)
    observacao = models.TextField('Observação', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado')
    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True, editable=False)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)
    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'

class Visita(models.Model):
    data_visita_ini = models.DateTimeField('Início da visita', default=datetime.datetime.today())
    data_visita_fim = models.DateTimeField('Fim da visita', blank=True, null=True)

    descricao = models.CharField('Descrição', max_length=200)
    tipo = models.CharField('Tipo de visita', max_length=2, choices=TIPO_VISITA, default='2')

    carro = models.ForeignKey(Carro)

    gasolina = models.DecimalField('Gasolina', max_digits=5, decimal_places=2, default='3.19', blank=True, null=True)
    km = models.PositiveSmallIntegerField('KM')
    valor_viagem = models.DecimalField('Valor da viagem', blank=True, null=True, max_digits=5, decimal_places=2)

    pago = models.BooleanField('Conta quitada', default=False)
    proposta = models.ForeignKey(Proposta, blank=True, null=True)

    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        self.valor_viagem =  "%0.2f" % math.ceil(self.km / self.carro.kmporlitro * self.gasolina)
        super(Visita, self).save(*args, **kwargs)
    def data_inicial_formatada(obj):
        return obj.data_visita_ini
    data_inicial_formatada.short_description = 'Data de visita'
    def __unicode__(self):
        if self.proposta.imovel:
            return "Visita %d - %s - %s" % (self.id, self.proposta.cliente.nome, self.proposta.imovel.nome)
        return "Sem imóvel"
    def data_visita_ini_formatada(self, obj):
        return obj.data_visita_ini.strftime("%d %b %Y %H:%M:%S")
    data_visita_ini_formatada.admin_order_field = 'data_visita_ini'
    data_visita_ini_formatada.short_description = 'Data da visita'