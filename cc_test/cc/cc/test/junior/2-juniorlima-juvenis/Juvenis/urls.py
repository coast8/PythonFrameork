# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView

from yawdadmin import admin_site

from core.view_admin import BuscaTagAdminView
from core.sitemaps import NoticiaSitemap, GaleriaSitemap, NoticiaBlogSitemap, NoticiaGoogleNewsSitemap, LetraSitemap, DownloadSitemap, LocalSitemap

admin.autodiscover()
admin_site._registry.update(admin.site._registry)
import settings

handler404 = 'noticias.views.erro'
handler500 = 'noticias.views.erro'

sitemaps = {
    'noticias': NoticiaSitemap,
    'galeria': GaleriaSitemap,
    'noticiablog': NoticiaBlogSitemap,
    'googlenews': NoticiaGoogleNewsSitemap,
    'letras': LetraSitemap,
    'download': DownloadSitemap,
    'local': LocalSitemap,
}

sitemapagoogle = {
    'googlenews': NoticiaGoogleNewsSitemap,
}

urlpatterns = patterns('',
    url(r'^admin/', include(admin_site.urls)),
    (r'^ckeditor/', include('lib.ckeditor.urls')),
    (r'^tag/', include('lib.tagging.urls')),
    (r'^tagging_autocomplete/', include('lib.tagging_autocomplete.urls')),
    url(r'^autocomplete-example/', BuscaTagAdminView.as_view(), name='autocomplete-example-view'),
    (r'^sitemap-googlenews\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemapagoogle,
                                                                         'template_name': 'extras/sitemap-googlenews.html'}),
    (r'^robots\.txt$', TemplateView.as_view(template_name="extras/robots.txt")),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps, 'template_name': 'extras/sitemap-googlenews.html'}),
)

urlpatterns += patterns('noticias.views',
    url(r'^$', 'homepage', name='homepage'),
    url(r'^contato/$', 'contato', name='contato'),
    (r'search', 'searchp'),

    url(r'^cantor/(?P<slugcantor>[\w_-]+)/$', 'cantor', name='cantor'),

    url(r'^download/$', 'downloads', name='downloads'),
    url(r'^download/(?P<slugcantor>[\w_-]+)/$', 'downloadcantor', name='downloadcantor'),
    url(r'^download/(?P<cantor_id>\d+)/(?P<download_id>\d+)/$', 'downloadlink', name='downloadlink'),
    url(r'^download/(?P<slugcantor>[\w_-]+)/(?P<slugalbum>[\w_-]+)/$', 'download', name='download'),


    url(r'^blog/$', 'blogs', name='blogs'),
    url(r'^blog/(?P<nomedoblog>[\w_-]+)/$', 'blog', name='blog'),
    url(r'^blog/(?P<slugblog>[\w_-]+)/(?P<slugnoticiablog>[\w_-]+)/$', 'noticiablog', name='noticiablog'),

    url(r'^fotos/$', 'galerias', name='fotos'),
    url(r'^fotos/(?P<sluggaleria>[\w_-]+)/$', 'galeria', name='galeria'),
    url(r'^fotos/(?P<galeria_id>\d+)/(?P<foto_id>\d+)/$', 'foto', name='foto'),

    url(r'^local/$', 'locais', name='locais'),
    url(r'^local/(?P<slugcidade>[\w_-]+)/(?P<slugdolocal>[\w_-]+)/$', 'local', name='local'),

    url(r'^shopping/$', 'produtos', name='produtos'),
    url(r'^shopping/(?P<slugcategoria>[\w_-]+)/(?P<slugproduto>[\w_-]+)/$', 'produto', name='produto'),

    url(r'^download/(?P<sluggenero>[\w_-]+)/$', 'genero', name='genero'),

    url(r'^letra/$', 'letras', name='letras'),
    url(r'^letra/(?P<slugcantor>[\w_-]+)/$', 'letracantor', name='letracantor'),
    url(r'^letra/(?P<slugcantor>[\w_-]+)/(?P<slugletra>[\w_-]+)/$', 'letra', name='letra'),

    url(r'^ultimas/$', 'ultimas', name='ultimas'),
    url(r'^(?P<slugcategoria>[\w_-]+)/$', 'categorianoticia', name='categorianoticia'),
    url(r'^(?P<slugcategoria>[\w_-]+)/(?P<slugestado>[\w_-]+)/(?P<slugcidade>[\w_-]+)/(?P<slug>[\w_-]+)/$', 'evento', name='evento'),
    url(r'^eventos/(?P<slugestado>[\w_-]+)/$', 'evento_estado', name='evento_estado'),
    url(r'^eventos/(?P<slugestado>[\w_-]+)/(?P<slugcidade>[\w_-]+)/$', 'evento_cidade', name='evento_cidade'),
    url(r'^(?P<slugcategoria>[\w_-]+)/(?P<slug>[\w_-]+)/$', 'noticia', name='noticia'),
)

if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Arquivos enviados pelo usuário
    urlpatterns += staticfiles_urlpatterns()