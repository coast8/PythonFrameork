# -*- coding: utf-8 -*-
__author__ = 'juniorlima'
from django.conf.urls import patterns, include, url
from django.contrib import admin

import settings

from django.contrib.sitemaps.views import sitemap
from assessoria.sitemap import BlogSitemap

sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drpessoa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
)

urlpatterns += patterns('assessoria.views',
    url(r'^$', 'index', name='index'),
    #url(r'^agenda/$', 'agenda', name='agenda'),
    url(r'^galeria/(?P<slug>[\w_-]+)/$', 'galeria', name='galeria'),
    url(r'^galeria/$', 'galerias', name='galerias'),
    url(r'^midia/$', 'namidia', name='namidia'),
    url(r'^amigos/$', 'amigos', name='amigos'),
    url(r'^noticia/(?P<slug>[\w_-]+)/$', 'noticia', name='noticia'),
    url(r'^noticia/$', 'noticias', name='noticias'),
    url(r'^perfil/$', 'perfil', name='perfil'),
    url(r'^timeline/$', 'timeline', name='timeline'),
    url(r'^voluntariado/$', 'voluntariado', name='voluntariado'),
    url(r'^contato/$', 'contato', name='contato'),
    )
