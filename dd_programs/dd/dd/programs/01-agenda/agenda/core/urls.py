from django.conf.urls import url

from agenda.core.views import home


urlpatterns = [
	url(r'^$', home, name='home'),
]
