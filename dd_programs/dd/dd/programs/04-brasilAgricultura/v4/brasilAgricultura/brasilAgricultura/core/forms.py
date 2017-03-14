from django import forms
from django.contrib.auth.models import User

from .models import Contato
from .models import Cliente

class ContatoForm(forms.ModelForm):
	mensagem = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Contato
		fields = ('nome', 'email', 'mensagem')

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ('nomeCompleto', 'endereco', 'cidade', 'cpf', 'dataNascimento')