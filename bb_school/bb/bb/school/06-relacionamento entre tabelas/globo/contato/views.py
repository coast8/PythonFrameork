from django.shortcuts import render

# Create your views here.

from .models import Contato

def contato(request):
	contato = Contato.objects.all()
	return render(request, 'contato/contato.html', {'contato': contato})