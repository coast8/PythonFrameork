# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'


from models import *
from django import forms
from django.contrib.localflavor.br.forms import BRPhoneNumberField

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
    telefoneresponsavel = BRPhoneNumberField(label = ('Telefone'), widget=forms.TextInput(attrs={'alt':'phone'}))
    telefonetecnico = BRPhoneNumberField(label = ('Telefone'), widget=forms.TextInput(attrs={'alt':'phone'}))

class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
    telefone = BRPhoneNumberField(label = ('Telefone'), widget=forms.TextInput(attrs={'alt':'phone'}))