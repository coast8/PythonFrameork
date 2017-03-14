from blog.categorias.models import Categoria

def categorias(request):
	return {
		'categorias': Categoria.objects.all()
	}