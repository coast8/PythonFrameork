# coding: utf-8

from django.conf.urls import patterns, url

from loja import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^cadastrar/$', views.salvar, name='cadastro'),
    url(r'^editar/(?P<pk>\d+)/$', views.editar, name='editar'),
    url(r'^remover/(?P<pk>\d+)/$', views.remover, name='remover'),
    url(r'^pesquisar/$', views.pesquisar, name='pesquisar'),
    # api
    url(r'^api/discos/$', views.disco_view, name='disco_view'),
    url(r'^api/discos/(?P<pk>[0-9]+)/$', views.disco_detail, name='disco_detail'),
)
