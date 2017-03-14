#modelos de forms

class ContactCourse(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )

'





from django import forms

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