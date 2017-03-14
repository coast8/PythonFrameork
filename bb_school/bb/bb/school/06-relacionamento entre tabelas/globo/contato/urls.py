from django.conf.urls import url

from globo.contato import views

urlpatterns = [
	url(r'informacoes/$', views.contato, name='informacoes'),
]