"""blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# padrao 
from django.conf.urls import include, url
from django.contrib import admin


# view para login e logout
from django.contrib.auth.views import login, logout


# views direto
from core import views

# views de forma indireta
from catalog import urls as catalog_urls
#from accounts import urls as accounts_urls

urlpatterns = [
    
    url(r'^$', views.index, name='index'),

    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^registro/$', views.register, name='register'),
	

    url(r'^catalogo/', include(catalog_urls, namespace='catalog')),
    #url(r'^conta/', include(accounts_urls, namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),
]
