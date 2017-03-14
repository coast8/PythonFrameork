# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django import forms
from django.contrib import admin
from cadastro.models import Membro

class MembroForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'vLargeTextField'}),)