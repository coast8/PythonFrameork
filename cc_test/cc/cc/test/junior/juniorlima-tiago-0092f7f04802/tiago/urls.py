"""tiago URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #url(r'^info/', include('informacao.urls', namespace='informacao')),
    url(r'^contato/', include('contato.urls', namespace='contato')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^sistema/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^filer/', include('filer.urls')),
    url(r'^', include('portal.urls', namespace='portal')),
    url(r'^gabinete/', include('gabinete.urls', namespace='gabinete')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


