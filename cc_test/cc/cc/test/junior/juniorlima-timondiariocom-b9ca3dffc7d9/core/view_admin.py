# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

import json
from django.views.generic import View
from django.http.response import HttpResponse
from django.core.exceptions import PermissionDenied

from letras.models import Album

from noticias.models import Noticias
# View para buscar em módulo

class BuscaTagAdminView(View):
    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise PermissionDenied

        query = request.GET.get('query', None)
        results = []

        for el in Noticias.objects.values_list('titulo', flat=True).distinct():
            if el and (not query or el.find(query.decode('utf-8')) != -1):
                results.append(el)

        return HttpResponse(json.dumps({'results': results}))
