from django import forms

from .models import Campanha

class CampanhaForm(forms.ModelForm):
	class Meta:
		model = Campanha
		exclude = ('data_criacao',)