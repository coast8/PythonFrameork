from django.conf.urls import url

from globo.posts import views

urlpatterns = [
	url(r'detalhes/(?P<post_id>\d+)/$', views.detalhes_post, name='detalhes'),
	url(r'categoria/(?P<categoria_id>\d+)/$', views.posts_por_categoria, name='posts_por_categoria'),
]
