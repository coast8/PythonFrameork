from django.conf.urls import url

from blog.contato import views

urlpatterns = [
	url(r'informacoes/$', views.contato, name='informacoes'),
]
