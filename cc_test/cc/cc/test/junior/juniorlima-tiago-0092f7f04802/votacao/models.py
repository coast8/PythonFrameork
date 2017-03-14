# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Voto(models.Model):
    nome_indicacao = models.CharField('Nome completo', max_length=100, unique=True)
    telefone = models.CharField('Telefone', max_length=15, default='869')
    titulo = models.CharField('Título', max_length=16, blank=True, null=True)
    zona = models.CharField('Zona', max_length=5, blank=True, null=True)
    secao = models.CharField('Seção', max_length=5, blank=True, null=True)
    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True, editable=False)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s - %s" % (self.nome_indicacao, self.usuario.get_full_name())
    class Meta:
        verbose_name = 'Meu voto'
        verbose_name_plural = 'Meus 40 votos'