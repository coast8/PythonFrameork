
##
## essa impotação ja é padrão
from django.conf.urls import url

## funções def que estamos importando 
from brasilAgricultura.core.views import index
from brasilAgricultura.core.views import quemsomos
from brasilAgricultura.core.views import produtos
from brasilAgricultura.core.views import contatos
from brasilAgricultura.core.views import extras


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^quem-somos/$', quemsomos, name='quemsomos'),
    url(r'^produtos/$', produtos, name='produtos'),
    url(r'^contatos/$', contatos, name='contatos'),
    url(r'^extras-/$', extras, name='extras'),
    
    ]

