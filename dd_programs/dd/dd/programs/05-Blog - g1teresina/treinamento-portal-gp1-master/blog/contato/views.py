from django.shortcuts import render

from .models import Contato
# Create your views here.

def contato(request):
	contato = Contato.objects.all()
	return render(request, 'contato/contato.html', {'contato': contato})