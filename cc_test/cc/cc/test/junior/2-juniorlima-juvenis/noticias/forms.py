# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django import forms
from django.core.urlresolvers import reverse_lazy

from yawdadmin.widgets import AutoCompleteTextInput, Select2Widget
from noticias.models import Noticias

class BuscarLocalEvento(forms.ModelForm):
    class Meta:
        widgets = {
            'local': Select2Widget(attrs={'style': 'width: 250px;'}),
        }

class BuscarCantorAlbum(forms.ModelForm):
    class Meta:
        widgets = {
            'cantor_nome': Select2Widget(attrs={'style': 'width: 250px;'}),
        }