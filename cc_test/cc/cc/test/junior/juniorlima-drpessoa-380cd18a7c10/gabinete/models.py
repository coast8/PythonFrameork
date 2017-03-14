# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'
import datetime

from django.contrib.auth.models import User
from django.db import models
from gabinete.br_states import STATE_CHOICES
from gabinete.choices import PESSOA_TIPO, PESSOA_GRUPO, PESSOA_SEXO, PESSOA_TRATAMENTO, PESSOA_ENDERECO, TELEFONE_TIPO, PESSOA_GRAU, SOLICITACAO_ASSUNTO, SOLICITACAO_STATUS, SOLICITACAO_PRIORIDADE, SOLICITACAO_TIPO

class Unidade(models.Model):
    nome = models.CharField('Unidade', max_length=50)

class Empresa(models.Model):
    nome = models.CharField('Unidade', max_length=50)

class Estado(models.Model):
    sigla = models.CharField('Sigla', max_length=2, unique=True)
    nome = models.CharField('Estado', max_length=20, unique=True)

class Cidade(models.Model):
    nome = models.CharField('Cidade', max_length=50)
    uf = models.ForeignKey(Estado)
    slugcidade = models.SlugField(max_length=100, blank=True, unique=True)

class Pessoa(models.Model):
    # PESSOA FISICA - BASICO
    ativo = models.BooleanField('Ativo', default=True)
    tipo = models.CharField('Tipo de Pessoa', max_length=2, default=1, choices=PESSOA_TIPO)
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('Email', max_length=70, blank=True, null=True)
    apelido = models.CharField('Nome de tratamento - Apelido', max_length=30, blank=True, null=True)
    site = models.URLField('Site', max_length=100, blank=True, null=True)
    unidadevinculada = models.ForeignKey(Unidade)
    gruposocial = models.CharField('Grupo Social', max_length=2, choices=PESSOA_GRUPO)
    sexo = models.CharField('Sexo', max_length=1, choices=PESSOA_SEXO)
    nascimento = models.DateField('Data de nascimento')
    foto = models.ImageField('Foto', upload_to='pessoa')
    notas = models.TextField('Notas')
    # INFORMAÇÕES ADICIONAIS
    tratamento = models.CharField('Tratamento', max_length=2, choices=PESSOA_TRATAMENTO, blank=True, null=True)
    empregador = models.ForeignKey(Empresa, blank=True, null=True)
    class Meta:
        verbose_name = 'Cadastro básico - Pessoa'
        verbose_name_plural = 'Cadastro básico - Pessoas'

class Logradouros(models.Model):
    endereco= models.CharField('Endereço', max_length=64, blank=True, null=True)
    cep = models.CharField('CEP', max_length=9, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=30, blank=True, null=True)
    cidade = models.CharField('Cidade', default='Teresina',max_length=40, blank=True, null=True)
    uf = models.CharField('UF', default='PI', max_length = 2, choices=STATE_CHOICES)
    tipo = models.CharField('Tipo de Endereço', max_length=2, choices=PESSOA_ENDERECO)
    correspondencia = models.BooleanField('Endereço para correspondência', default=True)
    class Meta:
        abstract = True

class Telefone(models.Model):
    telefone = models.CharField('Telefone', max_length=14)
    ramal = models.CharField('Ramal', max_length=5, blank=True, null=True)
    tipo = models.CharField('Tipo de telefone', max_length=2, choices=TELEFONE_TIPO)
    principal = models.BooleanField('Fone principal', default=None)
    pessoa = models.ForeignKey(Pessoa)


class Intermediario(Pessoa):
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)
    rg = models.CharField('RG', max_length=10, blank=True, null=True)
    orgaoemissor = models.CharField('Orgão Emissor', max_length=10, blank=True, null=True)
    cnpj = models.CharField('CNPJ', max_length=14, blank=True, null=True)
    razaosocial = models.CharField('Razão Social', max_length=50, blank=True, null=True)
    nomefantasia = models.CharField('Nome Fantasia', max_length=50, blank=True, null=True)
    class Meta:
        verbose_name = 'Cadastro intermediário - Pessoa'
        verbose_name_plural = 'Cadastro intermediário - Pessoas'

class Funcao(models.Model):
    nome = models.CharField('Nome', max_length=50)

class Avancado(Intermediario):
    # DADOS ELEITORAIS
    zonaeleitoral = models.CharField('Zona Eleitoral', max_length=20, blank=True, null=True)
    secao = models.CharField('Seção', max_length=20, blank=True, null=True)
    # NATURALIDADE
    cidade = models.ForeignKey(Cidade)
    # FILIAÇÃO
    pai = models.CharField('Pai', max_length=100, blank=True, null=True)
    mae = models.CharField('Mãe', max_length=100, blank=True, null=True)
    # INFORMAÇÕES ADICIONAIS
    escolaridade = models.CharField('Escolaridade', max_length=2, choices=PESSOA_GRAU, blank=True, null=True)
    funcao = models.ForeignKey(Funcao)
    class Meta:
        verbose_name = 'Cadastro completo - Pessoa'
        verbose_name_plural = 'Cadastro completo - Pessoas'

############################ PÚBLICO ############################
class Solicitacao(models.Model):
    # DADOS INICIAIS
    pessoa = models.ForeignKey(Pessoa)
    dataabertura = models.DateField('Data de abertura',)
    assunto = models.CharField('Assunto', max_length=2, choices=SOLICITACAO_ASSUNTO)
    areadeinteresse = models.CharField('Área de interesse', max_length=30)
    encaminhado = models.CharField('Encaminhado por', max_length=30, blank=True, null=True)
    unidade = models.ForeignKey(Unidade)
    solicitacao = models.TextField('Solicitação')
    # SOLICITAÇÃO
    status = models.CharField('Status', max_length=2, choices=SOLICITACAO_STATUS)
    prioridade = models.CharField('Prioridade', max_length=2, choices=SOLICITACAO_PRIORIDADE)
    tipo = models.CharField('Tipo de Recebimento', max_length=2, choices=SOLICITACAO_TIPO)

    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado', default=datetime.datetime.now())
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado', default=datetime.datetime.now())
    usuario = models.ForeignKey(User, related_name='user_add_sol', blank=True, editable=False, default=1)
    usuario_modificado = models.ForeignKey(User,  related_name='user_mod_sol', blank=True, default=1)
    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'

class AnexoSolicitacao(models.Model):
    anexo = models.FileField('Anexo da Solicitação', upload_to='anexosolicitacao')
    solicitacao = models.ForeignKey(Solicitacao)
    class Meta:
        verbose_name = 'Adicionar anexo à solicitação'
        verbose_name_plural = 'Adicionar anexos à solicitação'

class AndamentoSolicitacao(models.Model):
    # ANDAMENTO
    andamento = models.TextField('Andamento')
    solicitacao = models.ForeignKey(Solicitacao)
    data = models.DateField('Data do Andamento')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado', default=datetime.datetime.now())
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado', default=datetime.datetime.now())
    usuario = models.ForeignKey(User, related_name='user_add_and', blank=True, editable=False, default=1)
    usuario_modificado = models.ForeignKey(User,  related_name='user_mod_and', blank=True, default=1)
    class Meta:
        verbose_name = 'Andamento da solicitação'
        verbose_name_plural = 'Andamento da solicitação'

class Atendimento(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    dataabertura = models.DateTimeField('Data de abertura',)
    assunto = models.CharField('Assunto', max_length=2, choices=SOLICITACAO_ASSUNTO)
    unidade = models.ForeignKey(Unidade)
    atendimento = models.TextField('Atendimento')
    # ATENDIMENTO
    status = models.CharField('Status', max_length=2, choices=SOLICITACAO_STATUS)
    prioridade = models.CharField('Prioridade', max_length=2, choices=SOLICITACAO_PRIORIDADE)
    tipo = models.CharField('Tipo de Recebimento', max_length=2, choices=SOLICITACAO_TIPO)