# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

from core.choices import PUBLICIDADES_TIPOS

class Empresa(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True)

    telefone = models.CharField('Telefone', max_length=12, unique=True)
    email = models.CharField('Email', max_length=100, blank=True, null=True)

    responsavel = models.CharField('Responsavel', max_length=100, blank=True, null=True)
    telefoneresponsavel = models.CharField('Telefone', max_length=12, blank=True, null=True)

    website = models.URLField(max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to='empresas', blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, related_name='user_add_empresa', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_empresa', blank=True, null=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    def __unicode__(self):
        return  self.nome
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

class Formato(models.Model):
    ativo = models.BooleanField('Ativo', default=True)
    nome = models.CharField('Nome', max_length=50)
    tamanho = models.CharField('Tamanho', max_length=50)
    class Meta:
        verbose_name = 'Formato'
        verbose_name_plural = 'Formato'
    def __unicode__(self):
        return "%s - %s" % (self.nome, self.tamanho)

class Local(models.Model):
    ativo = models.BooleanField('Ativo', default=True)
    nome = models.CharField('Nome', max_length=50)
    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Local'
    def __unicode__(self):
        return self.nome

class Posicao(models.Model):
    ativo = models.BooleanField('Ativo', default=True)
    formato = models.ForeignKey(Formato)
    local = models.ForeignKey(Local)
    class Meta:
        unique_together = (("formato", "local"),)
        verbose_name = 'Posicionamento'
        verbose_name_plural = 'Posicionamento'
    def __unicode__(self):
        return "%s - %s - %s" % (self.formato.nome, self.formato.tamanho, self.local.nome)

class BasePublicidade(models.Model):
    """
    This is our base model, from which all ads will inherit.
    The manager methods for this model will determine which ads to
    display return etc.
    """
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=50)
    tipo = models.CharField('Tipo de publicidade', max_length=2, choices=PUBLICIDADES_TIPOS)
    posicao = models.ManyToManyField(Posicao)
    link = models.URLField(blank=True, null=True)

    dataentrada = models.DateTimeField('Data de entrada', default=datetime.now)
    datasaida = models.DateTimeField('Data de saída', default=datetime.now)

    empresa_nome = models.ForeignKey(Empresa, verbose_name='Empresa')

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    usuario = models.ForeignKey(User, blank=True, null=True)
    class Meta:
        abstract = True

class PubliTexto(BasePublicidade):
    """ a Model that describes the attributes and behaviours of ad zones """
    texto = models.TextField(verbose_name='Texto', max_length=100)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Publicidade - Texto'
        verbose_name_plural = 'Publicidade - Texto'


class PubliImagem(BasePublicidade):
    """ A standard banner Ad """
    arquivo = models.FileField(upload_to="arquivos/publicidade")
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Publicidade - Imagem'
        verbose_name_plural = 'Publicidade - Imagem'