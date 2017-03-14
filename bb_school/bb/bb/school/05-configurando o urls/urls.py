
from django.conf.urls import include, url
from django.contrib import admin

#IMPORTANDO O URL DE CORE
from mutirao.core import urls as core_urls

#IMPORTANDO O URL DE MULTIRÃO
from mutirao.campanha import urls as campanha_urls


urlpatterns = [
    url(r'', include(core_urls, namespace='core')),
    url(r'campanha/', include(campanha_urls, namespace='campanha')),
   
    url(r'^admin/', include(admin.site.urls)),
]