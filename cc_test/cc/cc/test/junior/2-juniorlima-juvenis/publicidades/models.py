# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


from core.choices import PUBLICIDADES_TIPOS
from core.thumbs import ImageWithThumbsField

from administrativo.models import Empresa

class BasePublicidade(models.Model):
    """
    This is our base model, from which all ads will inherit.
    The manager methods for this model will determine which ads to
    display return etc.
    """
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=50)
    tipo = models.CharField('Tipo de publicidade', max_length=2, choices=PUBLICIDADES_TIPOS)
    link = models.URLField(blank=True, null=True)

    dataentrada = models.DateTimeField('Data de entrada', default=datetime.now)
    datasaida = models.DateTimeField('Data de saída', )

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