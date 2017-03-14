# coding: utf-8

from django.db import models
from django.core.validators import MinValueValidator


class Genero(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=128)

    def __unicode__(self):
        return self.nome


class Cantor(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=128)

    def __unicode__(self):
        return self.nome


class Disco(models.Model):
    YEARS = [(i, i) for i in range(1900, 2015)]

    titulo = models.CharField(max_length=180)
    genero = models.ForeignKey(Genero, verbose_name="Genêro")
    cantor = models.ForeignKey(Cantor, verbose_name="Cantor")
    ano_lancamento = models.IntegerField(verbose_name="Ano lançamento", choices=YEARS, default=2014)
    valor = models.FloatField(verbose_name="Valor", validators=[MinValueValidator(0.01)])

    def __unicode__(self):
        return self.titulo