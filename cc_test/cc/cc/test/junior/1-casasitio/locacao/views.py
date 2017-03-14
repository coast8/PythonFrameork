# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.shortcuts import render, get_object_or_404

from locacao.models import Pagamento

def recibo(request, pagamento_id):
    pagamento = get_object_or_404(Pagamento, id=pagamento_id)
    return render(request, 'locacao/recibo.html', {
        'pagamento': pagamento,
    })