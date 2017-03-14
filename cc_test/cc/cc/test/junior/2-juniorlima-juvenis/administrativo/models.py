# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.db import models
from django.contrib.auth.models import User

from core.thumbs import ImageWithThumbsField
from core.destino_imagem import administrativo_empresa, administrativo_colaborador
#Empresa
class Empresa(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True)

    telefone = models.CharField('Telefone', max_length=12, unique=True)
    email = models.CharField('Email', max_length=100, blank=True, null=True)

    responsavel = models.CharField('Responsavel', max_length=100, blank=True, null=True)
    telefoneresponsavel = models.CharField('Telefone', max_length=12, blank=True, null=True)

    website = models.URLField(max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to=administrativo_empresa, blank=True, null=True)

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

class Colaboradores(models.Model):
    user = models.OneToOneField(User, related_name='user_colaborador_set')
    telefone = models.CharField(max_length=12)
    igreja = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.URLField(max_length=50, blank=True, null=True)
    plus = models.URLField(max_length=50, blank=True, null=True)
    fb_id = models.CharField('ID Facebook', max_length=50, blank=True, null=True)
    fb_username = models.CharField('Username Facebook', max_length=50, blank=True, null=True)
    foto = ImageWithThumbsField('Blogueiro Foto 1x1', upload_to='usuarios', sizes=((800,600),(300,225),(32,32)), blank=True, null=True)
    def __unicode__(self):
        return self.user.get_full_name()
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'