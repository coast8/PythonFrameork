

## impotaçao padrao
from django.conf.urls import include, url
from django.contrib import admin




## importa complemetar de app que cadastramos
## temos duas app cadastradas
##########################
###########################
from brasilAgricultura.core import urls as core_urls
from brasilAgricultura.contato import urls as contato_rols


## mapeamento das URLs
urlpatterns = [
	url(r'', include(core_urls, namespace='core')),
	#url(r'contato/', include(contato_urls, namespace='contato')),
    url(r'^admin/', include(admin.site.urls)),
]