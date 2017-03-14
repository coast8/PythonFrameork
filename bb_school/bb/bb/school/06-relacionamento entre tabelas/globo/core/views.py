from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from globo.posts.models import Post
from globo.categorias.models import Categoria

# Create your views here.

def home(request):
	lista_posts = Post.objects.all().order_by('-data_post')
	paginator = Paginator(lista_posts, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'posts/index.html', {'posts': posts})