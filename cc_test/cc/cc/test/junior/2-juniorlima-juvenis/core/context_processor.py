# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from blogs.models import NoticiaBlog
from noticias.models import Noticias


def estaticos_context_processor(request):
    destaque_home = Noticias.objects.filter(destaque=True, publicar=True).order_by('-criado_em')[:5]
    ultimas_home = Noticias.objects.filter(destaque=False, publicar=True).order_by('-criado_em')[:5]
    ultimas_blog = NoticiaBlog.objects.filter(publicar=True).order_by('-criado_em')[:5]
    return {
        'destaque_home': destaque_home,
        'ultimas_home': ultimas_home,
        'ultimas_blog': ultimas_blog,
    }