from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'addirceu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^filer/', include('filer.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('postagem.urls', namespace='postagem')),
    url(r'^agenda/$', 'postagem.views.agenda', name='agenda'),
    #url(r'^noticia/', include('postagem.urls', namespace='postagem')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
