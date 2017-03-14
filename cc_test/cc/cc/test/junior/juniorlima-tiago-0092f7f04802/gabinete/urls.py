from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

app_name = 'gabinete'


urlpatterns = [

    url(r'^visita/hoje/$', views.visita_do_dia, name='noticia'),
    #url(r'^visita/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$', views.visita_do_dia, name='visita_do_dia'),
]