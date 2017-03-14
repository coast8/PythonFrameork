from django.db import models
from django.db.models import F, DecimalField, ExpressionWrapper

from django.db.models import Count, Sum

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Historico(models.Model):
	descricao = models.CharField(max_length=50)

	#conta os historicos
	def quantidade(self):
		return self.historico_det.count()

	#deve fazer a soma dos campos 'valor' que foram contados pela function_quantidade
	def total(self):
		return self.historico_det.aggregate(total=models.Sum('valor'))['total']

	def __str__(self):
		return self.descricao

	class Meta:
		verbose_name = 'Historico'
		verbose_name_plural = 'Historicos'
		ordering = ['descricao']


class Pessoa(models.Model):

	nome = models.CharField(max_length=50)
	telefone = models.CharField(max_length=25, blank=True)
	

	class Meta:
		verbose_name = 'Pessoa'
		verbose_name_plural = 'Pessoas'
		ordering = ['nome']

	def __str__(self):
		return self.nome




CONTA_OPERACAO_DEBITO = 'd'
CONTA_OPERACAO_CREDITO = 'c'
#variável com uma tupla
#contendo as 2 variáveis anteriores, seguidas por seus respectivos rótulos
CONTA_OPERACAO_CHOICES = ((CONTA_OPERACAO_DEBITO, _('Debito')),(CONTA_OPERACAO_CREDITO, _('Credito')),)


CONTA_STATUS_APAGAR = 'a'
CONTA_STATUS_PAGO = 'p'
CONTA_STATUS_CHOICES = ((CONTA_STATUS_APAGAR, _('A Pagar')),(CONTA_STATUS_PAGO, _('Pago')),)

class Conta(models.Model):
	class Meta:
		ordering = ('-data_vencimento', 'valor')

	pessoa = models.ForeignKey(Pessoa)
	historico = models.ForeignKey(Historico, related_name='historico_det')
	data_vencimento = models.DateField()
	data_pagamento = models.DateField(null=True, blank=True)
	valor = models.DecimalField(max_digits=15, decimal_places=2)


	#argumento "choices" indica a tupla com a lista de opções de escolha.
	operacao = models.CharField(
		max_length=1, default=CONTA_OPERACAO_DEBITO, choices=CONTA_OPERACAO_CHOICES, blank=True,)

	status = models.CharField(
		max_length=1, default=CONTA_STATUS_APAGAR, choices=CONTA_STATUS_CHOICES, blank=True,)

	descricao = models.TextField(blank=True)


class ContaPagar(Conta):
	
	def save(self, *args, **kwargs):
		self.operacao = CONTA_OPERACAO_DEBITO
		super(ContaPagar, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'ContaPagar'
		verbose_name_plural = 'ContasPagas'


class ContaReceber(Conta):

	def save(self, *args, **kwargs):
		self.operacao = CONTA_OPERACAO_CREDITO
		super(ContaReceber, self).save(*args, **kwargs)	

	class Meta:
		verbose_name = 'ContaReceber'
		verbose_name_plural = 'ContasRecebidas'


#é abstrata, ou seja, não possui uma tabela no banco de dados
class Pagamento(models.Model):
	class Meta:
		abstract = True

	data_pagamento = models.DateField()
	valor = models.DecimalField(max_digits=15, decimal_places=2)

class PagamentoPago(Pagamento):
	conta = models.ForeignKey(ContaPagar)

	class Meta:
		verbose_name = 'PagamentoPago'
		verbose_name_plural = 'PagamentoPagos'

class PagamentoRecebido(Pagamento):
	conta = models.ForeignKey(ContaReceber)

	class Meta:
		verbose_name = 'PagamentoRecebido'
		verbose_name_plural = 'PagamentoRecebidos'