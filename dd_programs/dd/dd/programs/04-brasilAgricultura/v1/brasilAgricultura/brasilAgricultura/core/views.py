

## importação padrão
from django.shortcuts import render


## função para  a  página index
#############################
def index(request):
	return render(request, 'index.html')

def quemsomos(request):
	return render(request, 'quemsomos.html')

def produtos(request):
	return render(request, 'produtos.html')

def contatos(request):
	return render(request, 'contatos.html')

def extras(request):
	return render(request, 'extras.html')