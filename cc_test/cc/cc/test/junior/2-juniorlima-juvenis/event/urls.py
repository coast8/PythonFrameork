# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('event.views',
    url(r'^evento/(?P<slugevento>[\w_-]+)/$', 'evento', name='evento'),
    url(r'^evento/(?P<slugevento>[\w_-]+)/agrupar/$', 'agrupar', name='agrupar'),
    url(r'^evento/(?P<slugevento>[\w_-]+)/form/$', 'formevento', name='formevento'),
)