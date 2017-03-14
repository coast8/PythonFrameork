# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.template import Library, Node
from django.template.defaultfilters import stringfilter
import re

register = Library()

def paragraphs(value):
    """
    Turns paragraphs delineated with newline characters into
    paragraphs wrapped in <p> and </p> HTML tags.
    """
    paras = re.split(r'[\r\n]+', value)
    paras = ['<p>%s</p>' % p.strip() for p in paras]
    return '\n'.join(paras)
paragraphs = stringfilter(paragraphs)

register.filter(paragraphs)

@register.filter()
@stringfilter
def first_par(value):
    """
    Tome apenas o primeiro parágrafo do HTML passado.
    """
    return value.split("</p>")[0] + "</p>"