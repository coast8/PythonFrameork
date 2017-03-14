
from django.conf.urls import url

from Americano.boletimNoticias.views import home


urlpatterns = [
    url(r'^$', home, name='home'),

]