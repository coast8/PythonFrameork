# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.forms import ModelForm
from suit.widgets import AutosizedTextarea

from business.models import AndamentoProposta

class AndamentoPropostaForm(ModelForm):
    class Meta:
        model = AndamentoProposta
        exclude = []
        widgets = {
            'observacao': AutosizedTextarea(attrs={'class': 'input-medium', 'rows': 2, 'style': 'width:95%'}),
        }