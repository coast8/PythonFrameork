# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('locacao.views',
    url(r'^pagamento/(?P<pagamento_id>\d+)/$', 'recibo', name='recibo'),
)