# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.shortcuts import render


def recibo(request, pagamento_id):

    return render(request, 'locacao/recibo.html')