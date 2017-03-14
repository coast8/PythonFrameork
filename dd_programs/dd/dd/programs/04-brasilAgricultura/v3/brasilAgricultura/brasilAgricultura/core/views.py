

## importação padrão
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse


from .forms import ContatoForm
from .models import Cliente


## função para  a  página index
#############################
def index(request):
	return render(request, 'index.html')

def quemsomos(request):
	return render(request, 'quemsomos.html')

def produtos(request):
	return render(request, 'produtos.html')

def contatos(request):
	if request.method == 'POST':
		contato_form = ContatoForm(request.POST)

		if contato_form.is_valid():
			user = contato_form.save()
			user.save()
			return redirect('core:sucesso_usuario')
		else:
			print(contato_form.errors)
	else:
		contato_form = ContatoForm()

	return render(request, 'contatos.html',\
		{'contato_form': contato_form})

	

def sucesso_usuario(request):
	return render(request, 'core/sucesso_usuario.html')

def extras(request):
	return render(request, 'extras.html')








## estamos comproblema nesta função
## funcao que vai listar os clientes
def clientes(request):
	selectClientes = Cliente.objects.all()
	##return render(request, 'clientes.html')      ##isto é um dicionario
	return render(request, 'clientes.html', {'selectClientes': selectClientes})

def noticias(request):
	return render(request, 'noticias.html')

def pg404(request):
	return render(request, '404.html')

def pg500(request):
	return render(request, '500.html')