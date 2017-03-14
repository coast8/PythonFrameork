# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.template.context import RequestContext,Context
from django.shortcuts import render_to_response, get_object_or_404

from event.models import Evento, FotoCapa, Programacao, DiasdePalestra, Ministrante, GaleriaEvento, Patrocinio, Duvida, Testemunhal, Noticia, Ingresso
from event.forms import InscricaoForm, ParticipanteForm

def evento(request, slugevento):
    evento = get_object_or_404(Evento, slugevento=slugevento)
    foto_capa = FotoCapa.objects.filter(evento=evento)
    datas = DiasdePalestra.objects.filter(evento=evento)
    programacao = Programacao.objects.filter(evento=evento)
    ministrante = Ministrante.objects.filter(evento=evento)
    galeria = GaleriaEvento.objects.latest('id')
    patrocinadores = Patrocinio.objects.filter(evento=evento)
    perguntas = Duvida.objects.filter(evento=evento)
    testemunhais = Testemunhal.objects.filter(evento=evento)
    noticias = Noticia.objects.filter(evento=evento)
    return render_to_response('evento/home.html',locals(),context_instance=RequestContext(request))

def agrupar(request, slugevento):
    evento = get_object_or_404(Evento, slugevento=slugevento)
    programacao = Programacao.objects.all()
    datas = DiasdePalestra.objects.filter(evento=evento)

    return render_to_response('evento/agrupar.html',locals(),context_instance=RequestContext(request))
from django.contrib import messages

def formevento(request, slugevento):
    evento = get_object_or_404(Evento, slugevento=slugevento)
    if request.method == 'POST':
        form_participante = ParticipanteForm(request.POST)
        form_inscricao = InscricaoForm(data=request.POST, evento=evento.id)
        if form_inscricao.is_valid():
            part = form_participante.save(commit=False)
            part.evento = evento
            part.save()
            insc = form_inscricao.save(commit=False)
            insc.pessoa = part
            insc.evento = evento
            insc.save()
            return render_to_response('evento/form-com.html',locals(),context_instance=RequestContext(request))
        else:
            print form_inscricao.errors, form_participante.errors
    else:
        form_participante = ParticipanteForm()
        form_inscricao = InscricaoForm(evento=evento.id)

    return render_to_response('evento/form.html',locals(),context_instance=RequestContext(request))