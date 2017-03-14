# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.db import models
from django.db.models import signals
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from lib.sorl.thumbnail import ImageField

from core.models import Noticia
from core.thumbs import ImageWithThumbsField
from core.destino_imagem import galeria_album


def destino_imagem_galeria(instance, filename):
    return '/'.join(['fotos', str(instance.galeria.slug), filename])

class Galeria(Noticia):
    chamada = models.CharField(max_length=30)
    imagem = ImageWithThumbsField('Imagem Destaque', upload_to=galeria_album, sizes=((800,600),(300,225)), max_length=150)
    subtitulo = models.CharField(max_length=200)
    def __unicode__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse('noticias.views.galeria', kwargs={'sluggaleria': self.slug})

class FotoGaleria(models.Model):
    nome = models.CharField(max_length=50)
    img = ImageField('Imagem do projeto', upload_to=destino_imagem_galeria, max_length=200)
    galeria = models.ForeignKey(Galeria, blank=True, null=True, related_name='foto_galeria_set')
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    def __unicode__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('noticias.views.foto', kwargs={'galeria_id': self.galeria_id,
                                                      'foto_id':self.id,})

    def url(self):
        return reverse('imagem', args=(self.slug,))

    def imagemAdmin(self):
        from sorl.thumbnail import get_thumbnail
        if self.img:
            try:
                im = get_thumbnail(self.img, '170x127')
                return '<img src="{0}" />'.format(im.url)
            except:
                return ''
        return ''
    imagemAdmin.is_safe = True
    imagemAdmin.allow_tags = True
    imagemAdmin.short_description = u'Imagem'

def galeria_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(galeria_pre_save, sender=Galeria)