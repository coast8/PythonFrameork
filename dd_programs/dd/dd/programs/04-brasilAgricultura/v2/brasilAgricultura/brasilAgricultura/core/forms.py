from django import forms
from django.contrib.auth.models import User

from .models import Contato


class ContatoForm(forms.ModelForm):
	mensagem = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Contato
		fields = ('nome', 'email', 'mensagem')
