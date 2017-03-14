# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django import forms
from django.core.urlresolvers import reverse_lazy

from yawdadmin.widgets import AutoCompleteTextInput, Select2Widget

class BuscarAlbumAdminForm(forms.ModelForm):
    class Meta:
        widgets = {
            'nome': AutoCompleteTextInput(source=\
                                    reverse_lazy('autocomplete-example-view')),
            'album_nome': Select2Widget(attrs={'style': 'width: 250px;'}),
        }
