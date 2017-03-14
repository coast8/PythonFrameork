from django.shortcuts import render
from contato.models import Pessoa

def home(request):
    pessoas_list = Pessoa.objects.all().order_by('bairro__nome')
    return render(request, 'sistema/contatos.html', {
        'pessoas_list': pessoas_list,
    })
