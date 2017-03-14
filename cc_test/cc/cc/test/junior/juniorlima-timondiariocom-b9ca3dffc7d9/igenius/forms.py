# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django import forms
from django.core.urlresolvers import reverse_lazy

from yawdadmin.widgets import AutoCompleteTextInput, Select2Widget, SwitchWidget
from noticias.models import Noticia


class NoticiaAdd(forms.ModelForm):
    class Meta:
        widgets = {
            'publicar': SwitchWidget(attrs={'class': 'switch-small'}),
            'manchete': SwitchWidget(attrs={'class': 'switch-small'}),
            'extra': SwitchWidget(attrs={'class': 'switch-small'}),
            'usarVideo': SwitchWidget(attrs={'class': 'switch-small'}),
            'autor': Select2Widget(attrs={'style': 'width: 205px;'}),
            'subcategoria': Select2Widget(attrs={'style': 'width: 210px;'}),
            'time': Select2Widget(attrs={'style': 'width: 210px;'}),
            'campeonato': Select2Widget(attrs={'style': 'width: 210px;'}),
            'fonte': Select2Widget(attrs={'style': 'width: 210px;'}),

        }

class PublicidadeAdd(forms.ModelForm):
    class Meta:
        widgets = {
            'publicar': SwitchWidget(attrs={'class': 'switch-small'}),
            'manchete': SwitchWidget(attrs={'class': 'switch-small'}),
            'extra': SwitchWidget(attrs={'class': 'switch-small'}),
            'usarVideo': SwitchWidget(attrs={'class': 'switch-small'}),
            'autor': Select2Widget(attrs={'style': 'width: 205px;'}),
            'subcategoria': Select2Widget(attrs={'style': 'width: 210px;'}),
            'fonte': Select2Widget(attrs={'style': 'width: 210px;'}),

        }


class BlogNoticia(forms.ModelForm):
    class Meta:
        widgets = {
            'publicar': SwitchWidget(attrs={'class': 'switch-small'}),
            'destaque': SwitchWidget(attrs={'class': 'switch-small'}),
            'blog': Select2Widget(attrs={'style': 'width: 210px;'}),

        }

class GamesForms(forms.ModelForm):
    class Meta:
        widgets = {
            'publicar': SwitchWidget(attrs={'class': 'switch-small'}),
            'destaque': SwitchWidget(attrs={'class': 'switch-small'}),
            'down': SwitchWidget(attrs={'class': 'switch-small'}),
            'usarVideo': SwitchWidget(attrs={'class': 'switch-small'}),
            'posicao': Select2Widget(attrs={'style': 'width: 210px;'}),
            'nomecategoria': Select2Widget(attrs={'style': 'width: 210px;'}),
            'subcategoria': Select2Widget(attrs={'style': 'width: 210px;'}),
            'genero': Select2Widget(attrs={'style': 'width: 210px;'}),
            'sistema': Select2Widget(attrs={'style': 'width: 210px;'}),
            'licenca': Select2Widget(attrs={'style': 'width: 210px;'}),
            'empresa': Select2Widget(attrs={'style': 'width: 210px;'}),
            'autor': Select2Widget(attrs={'style': 'width: 210px;'}),

        }
