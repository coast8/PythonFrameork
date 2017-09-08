from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

# Create your views here.

def detalhes_post(request, post_id):
	post = Post.objects.get(id=post_id)
	return render(request, 'posts/detalhes_post.html', {'post': post})

def posts_por_categoria(request, categoria_id):
	lista_de_categorias = Post.objects.filter(categoria=categoria_id)
	paginator = Paginator(lista_de_categorias, 5)
	page = request.GET.get('page')
	try:
		posts_categoria = paginator.page(page)
	except PageNotAnInteger:
		posts_categoria = paginator.page(1)
	except EmptyPage:
		posts_categoria = paginator.page(paginator.num_pages)
	return render(request, 'posts/posts_categoria.html', {'posts_categoria': posts_categoria})