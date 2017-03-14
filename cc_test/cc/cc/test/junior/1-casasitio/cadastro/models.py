# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

from core.models import Logradouros
from core.choices import TIPO_CLIENTE, ORIGEM_CHOICES, OPERADORA_CHOICES, TIPO_CONTA_CHOICES

class TipodeConta(models.Model):
    nome = models.CharField('Tipo de Receita', max_length=50, unique=True)
    tipo = models.CharField('Tipo de conta', max_length=2, choices=TIPO_CONTA_CHOICES)
    def __unicode__(self):
        return self.nome

class Carro(models.Model):
    ativo = models.BooleanField('Ativo', default=True)
    modelo = models.CharField('Modelo do carro', max_length=30)
    dono = models.CharField('Dono do carro', max_length=30)
    placa = models.CharField('Placa', max_length=8)
    cor = models.CharField('Cor', max_length=15)
    kmporlitro = models.PositiveSmallIntegerField('Quilômetro por litros')
    class Meta:
        verbose_name = 'Visitas - Carro'
        verbose_name_plural = 'Visitas - Carros'
    def __unicode__(self):
        return "%s - %s" % (self.modelo, self.dono)

class PreCliente(Logradouros):
    ativo = models.BooleanField('Ativo', default=True)
    tipo = models.CharField('Tipo de cliente', max_length=2, choices=TIPO_CLIENTE, blank=True, default='1')
    identificacao = models.CharField('Identificação', max_length=100, blank=True, null=True)
    nome = models.CharField('Nome', max_length=30)
    nome_completo = models.CharField('Nome Completo', max_length=100, unique=True, blank=True, null=True)
    origem = models.CharField('Origem', max_length=2, choices=ORIGEM_CHOICES, default=2)

    operadora = models.CharField('Operadora', max_length=2, choices=OPERADORA_CHOICES, default='1')
    telefone = models.CharField('Telefone', max_length=15)
    operadora_adc = models.CharField('Operadora 2', max_length=2, choices=OPERADORA_CHOICES, blank=True, null=True)
    telefone_adc = models.CharField('Telefone 2', max_length=15, blank=True, null=True)

    observacao = RichTextField('Observação', blank=True, null=True)
    email = models.EmailField('Email', max_length=50, blank=True, null=True)

    facebook = models.CharField('Facebook', max_length=30,blank=True, null=True)
    instagram = models.CharField('Instagram', max_length=30,blank=True, null=True)

    # Pessoa Física
    data_nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    telefone_extra = models.CharField('Telefone', max_length=15, blank=True, null=True)
    rg = models.CharField('RG', max_length=20, blank=True, null=True)
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)

    # Pessoa Jurídica
    cnpj = models.CharField('CNPJ', max_length=20, blank=True, null=True)
    razao_social = models.CharField('Razão Social', max_length=100, blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True, editable=False)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)
    def __unicode__(self):
        return "%s - %s - %s" % (self.nome, self.get_operadora_display(), self.telefone)

class Cliente(PreCliente):
    class Meta:
        proxy = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Proprietario(Logradouros):
    ativo = models.BooleanField('Ativo', default=True)
    nome = models.CharField('Nome Completo', max_length=100)
    apelido = models.CharField('Nome que gosta de ser chamado', max_length=30)
    rg = models.CharField('RG', max_length=20, blank=True, null=True)
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)
    operadora = models.CharField('Operadora', max_length=2, choices=OPERADORA_CHOICES, default='1')
    telefone = models.CharField('Telefone', max_length=15)
    operadora_adc = models.CharField('Operadora', max_length=2, choices=OPERADORA_CHOICES, default='1', blank=True, null=True)
    telefone_adc = models.CharField('Telefone', max_length=15, blank=True, null=True)
    telefone_extra = models.CharField('Telefone', max_length=15, blank=True, null=True)

    email = models.EmailField('Email', max_length=50, blank=True, null=True)
    profissao = models.CharField('Profissão', max_length=50, blank=True, null=True)
    datanascimento = models.DateField('Data de nascimento', blank=True, null=True)

    caseiro = models.CharField('Nome do caseiro', max_length=100, blank=True, null=True)
    telefone_caseiro = models.CharField('Telefone', max_length=15, blank=True, null=True)

    observacoes = RichTextField('Observações', blank=True, null=True)
    def __unicode__(self):
        return "%s - %s - %s" % (self.nome, self.get_operadora_display(), self.telefone)