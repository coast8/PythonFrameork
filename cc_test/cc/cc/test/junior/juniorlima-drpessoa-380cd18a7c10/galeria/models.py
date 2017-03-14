# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import signals
from django.template.defaultfilters import slugify

from assessoria.models import Postagem
class Galeria(Postagem):
    class Meta:
        verbose_name = 'Álbum de foto'
        verbose_name_plural = 'Álbum de fotos'
    def save(self, *args, **kwargs):
        self.categoria_id= 4
        super(Galeria, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('assessoria.views.galeria', kwargs={'slug': self.slug})

class Image(models.Model):
    file = models.FileField('Foto', upload_to='images/')
    galeria = models.ForeignKey('Galeria', related_name='images', blank=True, null=True)

    def __str__(self):
        return self.filename

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'


def galeria_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(galeria_pre_save, sender=Galeria)