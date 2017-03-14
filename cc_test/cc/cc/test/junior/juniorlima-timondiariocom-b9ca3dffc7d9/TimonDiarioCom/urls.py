# -*- coding: utf-8 -*-
__author__ = 'Junior Rodrigues'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from yawdadmin import admin_site

admin.autodiscover()
admin_site._registry.update(admin.site._registry)
admin_site.register_top_menu_item('igenius', icon_class="icon-th")
admin_site.register_top_menu_item('noticias', icon_class="icon-th")
admin_site.register_top_menu_item('blogs', icon_class="icon-th")
admin_site.register_top_menu_item('auth', icon_class="icon-th")
admin_site.register_top_menu_item('times', icon_class="icon-th")
#admin_site.register_top_menu_item('games', icon_class="icon-th")
admin_site.register_top_menu_item('publicidades', icon_class="icon-th")
import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin_site.urls)),
    (r'^ckeditor/', include('lib.ckeditor.urls')),
    (r'^assunto/(?P<slugcategoria>[\w_-]+)/', include('lib.tagging.urls')),
    (r'^tagging_autocomplete/', include('lib.tagging_autocomplete.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += patterns('',
    (r'^blogs', 'igenius.views.blogs'),
    (r'^contato', 'igenius.views.contato'),
    (r'^sobre', 'igenius.views.sobre'),
    (r'^blog/(?P<slugblog>[\w_-]+)/(?P<slug>[\w_-]+)/$', 'igenius.views.noticiablog'),
    (r'^blog/(?P<slugblog>[\w_-]+)', 'igenius.views.bloghome'),

    (r'^(?P<slugcategoria>[\w_-]+)/(?P<slugsubcategoria>[\w_-]+)/times/(?P<slugtime>[\w_-]+)/(?P<slugnoticia>[\w_-]+)/$', 'igenius.views.noticiatime'),

    (r'busca-blog','igenius.views.buscablog'),

    (r'^esportes/futebol/times/(?P<slugtime>[\w_-]+)$', 'igenius.views.timeInterna'),
    (r'^esportes/futebol/times/(?P<slugtime>[\w_-]+)/$', 'igenius.views.timeInterna'),
    (r'^esportes/futebol/times/(?P<slugtime>[\w_-]+)/noticias$', 'igenius.views.timemais'),

    (r'busca','igenius.views.busca'),

    (r'^(?P<slugcategoria>[\w_-]+)/(?P<slugsubcategoria>[\w_-]+)/$', 'igenius.views.subcategoria'),
    (r'^(?P<slugcategoria>[\w_-]+)/(?P<slugsubcategoria>[\w_-]+)$', 'igenius.views.subcategoria'),

    (r'^noticia/(?P<slugcategoria>[\w_-]+)/(?P<slugsubcategoria>[\w_-]+)/(?P<slugnoticia>[\w_-]+)/$', 'igenius.views.noticiainterna'),

    (r'^(?P<sluguf>[\w_-]+)/(?P<slugcidade>[\w_-]+)/(?P<slugbairro>[\w_-]+)', 'igenius.views.bairro'),

    (r'^publicidade/(?P<slugpublicidade>[\w_-]+)', 'igenius.views.patrocinado'),

    (r'^(?P<slugcategoria>[\w_-]+)', 'igenius.views.categoria'),

    (r'^$', 'igenius.views.homepage'),


)

if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Arquivos enviados pelo usuário
    urlpatterns += staticfiles_urlpatterns()