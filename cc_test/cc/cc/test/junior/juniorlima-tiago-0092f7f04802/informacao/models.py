from __future__ import unicode_literals
# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

import datetime
from django.db import models
from django.core.urlresolvers import reverse

from contato.models import Pessoa, Bairro, Lideranca

class Visita(models.Model):
    data_visita = models.DateTimeField('Data', default=datetime.datetime.now())
    acompanhantes = models.ManyToManyField('contato.Coordenacao')
    endereco = models.CharField('Endereço', max_length=100, blank=True, null=True)
    lideranca = models.ForeignKey(Lideranca)
    bairro = models.ForeignKey(Bairro)
    def __unicode__(self):
        return "%s - %s - %s" % (self.bairro.nome, self.data_visita.strftime("%d/%m"), self.lideranca)


class Participantes(Pessoa):
    visita = models.ForeignKey(Visita)
    def save(self, *args, **kwargs):
        self.bairro_id = self.visita.bairro_id
        super(Participantes, self).save()
    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'