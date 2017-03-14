from django.conf.urls import url

from multirao.campanha import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^adicionar/$', views.add_campanha, name='add_campanha'),
]
