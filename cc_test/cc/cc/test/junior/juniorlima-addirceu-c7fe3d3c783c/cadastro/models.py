# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.db import models
from django.contrib.auth.models import User

from cadastro.choices import ESTADO_CIVIL, SEXO, ESCOLARIDADE
from cadastro.br_states import STATE_CHOICES

class Departamento(models.Model):
    nome = models.CharField('Departamento', max_length=10, unique=True)

class Logradouros(models.Model):
    endereco = models.CharField('Endereço', max_length=64, blank=True, null=True)
    cep = models.CharField('CEP', max_length=9, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=30, blank=True, null=True)
    cidade = models.CharField('Cidade', default='Teresina',max_length=40, blank=True, null=True)
    uf = models.CharField('UF', default='PI', max_length = 2, choices=STATE_CHOICES)
    class Meta:
        abstract = True

class Congregacao(models.Model):
    nome = models.CharField('Nome', max_length=30, unique=True)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Congregação'
        verbose_name_plural = 'Congregações'

class Funcao(models.Model):
    nome = models.CharField('Nome', max_length=30, unique=True)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'
class Profissao(models.Model):
    nome = models.CharField('Nome', max_length=30, unique=True)

class Cadastro(models.Model):
    ativo = models.BooleanField('Ativo', default=True)
    obreiro = models.BooleanField('Obreiro', default=False)
    nome = models.CharField('Nome', max_length=100, unique=True)
    profissao = models.ForeignKey(Profissao, blank=True, null=True)
    estado_civil = models.CharField('Estado Civil', max_length=2, choices=ESTADO_CIVIL)
    sexo = models.CharField('Sexo', max_length=2, choices=SEXO)
    escolaridae = models.CharField('Escolaridade', max_length=2, choices=ESCOLARIDADE, blank=True, null=True)
    data_nascimento = models.DateField('Data de Nascimento',)
    cpf = models.CharField(max_length = 11, blank=True, null=True)
    rg = models.CharField(max_length = 11, blank=True, null=True)
    orgao_expedidor = models.CharField(max_length = 5, default='SSP')
    ug_orgao = models.CharField(max_length = 2, default='PI')
    pai = models.CharField('Pai', max_length=100, blank=True, null=True)
    mae = models.CharField('Mãe', max_length=100, blank=True, null=True)
    email = models.EmailField('Email', max_length=50, blank=True, null=True)
    titulo_eleitor = models.EmailField('Título de eleitor', max_length=15, blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=15)
    telefone_adc = models.CharField('Telefone', max_length=15, blank=True, null=True)
    data_espirito = models.DateField('Data - Batismo no espírito santo', blank=True, null=True)
    data_aguas = models.DateField('Data - Batismo nas águas', blank=True, null=True)
    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True, editable=False)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Cadastro'
        verbose_name_plural = 'Cadastros'

class Membro(Cadastro):
    class Meta:
        proxy=True

class Cargo(models.Model):
    ativo = models.BooleanField('Ativo', default=True)
    funcao = models.ForeignKey(Funcao)
    data_inicial = models.DateField('Data inicial', )
    data_final = models.DateField('Data final', blank=True, null=True)
    obreiro = models.ForeignKey(Membro)
    def __unicode__(self):
        return self.obreiro.nome
    class Meta:
        verbose_name = 'Trabalhador'
        verbose_name_plural = 'Trabalhadores'