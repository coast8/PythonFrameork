# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

from cadastro.models import TipodeConta
from core.choices import PAGAMENTO_TIPO

class Fechamento(models.Model):
    quitado = models.BooleanField('Pagamento', default=False)

    proposta = models.ForeignKey('business.Proposta')

    datainicio = models.DateTimeField('Data de chegada')
    datafim = models.DateTimeField('Data de partida')

    valorfechado = models.DecimalField('Valor do contrato', max_digits=6, decimal_places=2)
    valor_proprietario = models.DecimalField('Valor para o proprietário', max_digits=6, decimal_places=2)
    lucro = models.DecimalField('Lucro', max_digits=6, decimal_places=2, blank=True, null=True)

    dados_contrato = RichTextField('Dados específicos de contrato', blank=True, null=True)
    observacao = RichTextField('Observação', blank=True, null=True)

    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True, editable=False)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        if not self.id:
            if not self.lucro:
                self.lucro = self.valorfechado - self.valor_proprietario
        super(Fechamento, self).save(*args, **kwargs)
    def data_inicio_in(self):
        return self.datainicio.strftime('%d/%m/%Y')
    data_inicio_in.short_description = 'Data do evento'
    data_inicio_in.admin_order_field = 'datainicio'
    def data_fechamento_in(self):
        return self.criado_em.strftime('%d/%m/%Y')
    data_fechamento_in.short_description = 'Fechamento'
    data_fechamento_in.admin_order_field = 'criado_em'
    def __unicode__(self):
        if self.proposta.imovel:
            return "%i - %s - %s - %s - %s" % (self.id, self.proposta.cliente.nome, self.proposta.imovel.proprietario.apelido, self.proposta.imovel.nome, self.datainicio.strftime('%d/%m/%Y'))
        return "%i - %s - Escolha imóvel - %s" % (self.id, self.proposta.cliente.nome, self.datainicio.strftime('%d/%m/%Y'))

def get_upload_to(instance, filename):
    return '/'.join(['documentos', '%Y', str(instance.fechamento.id), filename])

class Documento(models.Model):
    nome = models.CharField('Nome', max_length=30)
    #arquivo = models.FileField('Arquivo de documento', upload_to='documentos/%Y/%m/')
    arquivo = models.FileField('Arquivo de documento', upload_to=get_upload_to)
    fechamento = models.ForeignKey(Fechamento)
    def __unicode__(self):
        return self.nome

class Pagamento(models.Model):
    # Pagamento
    recebido = models.BooleanField('Pago', default=False)
    tipo_receita = models.ForeignKey(TipodeConta)
    tipo_recebimento = models.CharField('Tipo de pagamento', max_length=2, choices=PAGAMENTO_TIPO)
    valor = models.DecimalField('Valor de pagamento', max_digits=10, decimal_places=2)
    lucro = models.DecimalField('Lucro Sítios', max_digits=10, decimal_places=2)
    repasse = models.DecimalField('Valor para o dono', max_digits=10, decimal_places=2)
    fechamento = models.ForeignKey(Fechamento)
    # Recebimento
    prazo_recebimento = models.DateField('Prazo para pagamento',)
    data_recebimento = models.DateField('Data do pagamento', blank=True, null=True)
    recebimento = models.CharField('Recebido por', max_length=100, blank=True, null=True)
    pagante = models.CharField('Pago por', max_length=100, blank=True, null=True)
    # Repasse
    data_entrega = models.DateField('Data do repasse', blank=True, null=True)
    entregue = models.CharField('Entregue para', max_length=100, blank=True, null=True)

    observacao = RichTextField('Observação', blank=True, null=True)

    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True, editable=False)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s - %s - R$ %d" % (self.fechamento.proposta.cliente.nome, self.fechamento.proposta.imovel.nome, self.valor)