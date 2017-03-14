"""multirao URL Configuration


	URL PAI
"""





from django.conf.urls import include, url
from django.contrib import admin

from multirao.core import urls as core_urls
from multirao.campanha import urls as campanha_urls 


urlpatterns = [
	url(r'', include(core_urls, namespace='core')),
	url(r'campanha/', include(campanha_urls, namespace='campanha')),
    url(r'^admin/', include(admin.site.urls)),
]
