# coding: utf-8

from django import forms

from django.forms import ModelForm

from loja.models import Disco,Cantor, Genero


class DiscoForm(ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Disco
