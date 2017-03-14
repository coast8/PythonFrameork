# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django import forms
from django.forms import ModelForm

from event.models import Inscricao, Participante, Ingresso, Evento

class InscricaoForm(ModelForm):
    class Meta:
        model = Inscricao
        exclude = ('evento', 'pessoa')
    ingresso = forms.ModelChoiceField(queryset = Ingresso.objects.none())

    def __init__(self, evento, *args, **kwargs):
        super(InscricaoForm, self).__init__(*args, **kwargs)
        self.fields['ingresso'].queryset = Ingresso.objects.filter(evento = evento)


class ParticipanteForm(ModelForm):
    class Meta:
        model = Participante
        exclude = ('publicar', 'foto', 'apelido', 'evento')
    nome = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    telefone = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Telefone'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))