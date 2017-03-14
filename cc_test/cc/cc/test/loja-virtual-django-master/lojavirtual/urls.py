from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns

from loja import views


urlpatterns = patterns('',
    url(r'^loja/', include('loja.urls', namespace='loja')),
)


urlpatterns = format_suffix_patterns(urlpatterns)