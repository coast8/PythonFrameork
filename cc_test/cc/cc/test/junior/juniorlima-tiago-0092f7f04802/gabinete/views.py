# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render

from gabinete.models import AtendimentoGabinete
def visita_do_dia(request):
    from datetime import datetime
    dt = datetime.now()
    start = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    end = dt.replace(hour=23, minute=59, second=59, microsecond=999999)
    atendimentos = AtendimentoGabinete.objects.filter(data_chegada__range=(start,end))
    return render(request, 'portal/visitadodia.html', {
        'atendimentos': atendimentos,
        'dt': dt,
    })
