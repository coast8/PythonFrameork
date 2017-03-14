# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'


from django.template.defaultfilters import slugify

def letra_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

def cantor_pre_save(signal, instance, sender, **kwargs):
    instance.slugcantor = slugify(instance.nome)