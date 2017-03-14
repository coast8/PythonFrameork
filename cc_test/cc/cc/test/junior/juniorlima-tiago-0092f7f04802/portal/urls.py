from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

app_name = 'portal'


urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^(?P<slugcategoria>[\w_-]+)/(?P<slug>[\w_-]+)/$', views.noticia, name='noticia'),
]