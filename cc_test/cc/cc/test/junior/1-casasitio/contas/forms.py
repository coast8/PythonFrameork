# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django import forms
from django.contrib.auth.models import User

from contas.models import Usuario

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('telefone', 'data_nascimento')
