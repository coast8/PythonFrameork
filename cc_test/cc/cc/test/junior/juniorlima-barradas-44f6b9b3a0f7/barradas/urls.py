from django.conf.urls import patterns, include, url
from django.contrib import admin

import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'barradas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin_tools/', include('admin_tools.urls')),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('portal.views',
    url(r'^$', 'home', name='home'),
    url(r'^noticia/$', 'noticias', name='noticias'),
    url(r'^noticia/(?P<slug>[\w_-]+)$', 'noticia', name='noticia'),
    url(r'^(?P<slug>[\w_-]+)$', 'categoria', name='categoria'),
    url(r'^(?P<slug>[\w_-]+)/$', 'blog', name='blog'),
    url(r'^(?P<blog>[\w_-]+)/(?P<slug>[\w_-]+)/$', 'noticia_blog', name='noticia_blog'),
    )