# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib.sitemaps import Sitemap

from noticias.models import Noticias, Album
from galeria.models import Galeria
from blogs.models import NoticiaBlog
from letras.models import Letra
from locais.models import Local

class NoticiaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Noticias.objects.filter(publicar=True).exclude(categoria_nome=6).order_by('-criado_em')

    def lastmod(self, obj):
        return obj.criado_em

from django.template.response import TemplateResponse

class NoticiaGoogleNewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Noticias.objects.filter(publicar=True, categoria_nome=6).order_by('-criado_em')

    def lastmod(self, obj):
        return obj.criado_em


class GaleriaSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Galeria.objects.filter(publicar=True).order_by('-criado_em')

    def lastmod(self, obj):
        return obj.criado_em

class NoticiaBlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return NoticiaBlog.objects.filter(publicar=True).order_by('-criado_em')

    def lastmod(self, obj):
        return obj.criado_em

class LetraSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Letra.objects.filter(publicar=True).order_by('-criado_em')

    def lastmod(self, obj):
        return obj.criado_em

class DownloadSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Album.objects.filter(publicar=True).order_by('-criado_em')

    def lastmod(self, obj):
        return obj.criado_em

class LocalSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.5

    def items(self):
        return Local.objects.filter(publicar=True).order_by('-criado_em')

    def lastmod(self, obj):
        return obj.criado_em