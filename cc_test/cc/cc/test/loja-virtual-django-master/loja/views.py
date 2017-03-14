# coding: utf-8

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from loja.forms import DiscoForm
from loja.models import Cantor, Disco, Genero
from loja.serializers import CantorSerializer, DiscoSerializer, GeneroSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def disco_view(request, format=None):

    if request.method == 'GET':
        discos = Disco.objects.all()
        serializer = DiscoSerializer(discos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DiscoSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def disco_detail(request, pk, format=None):
    try:
        disco = Disco.objects.get(pk=pk)
    except Disco.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = DiscoSerializer(disco)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DiscoSerializer(disco, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        disco.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    discos = Disco.objects.all().order_by('valor')

    paginator = Paginator(discos, 4)

    page = request.GET.get('page')

    try:
        page_disco = paginator.page(page)
    except PageNotAnInteger:
        page_disco = paginator.page(1)
    except EmptyPage:
        page_disco = paginator.page(page.num_pages)

    return render(request, 'loja/index.html', {'list_discos': page_disco})


def salvar(request):
    form = DiscoForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            form_clean = form.cleaned_data
            pk = form_clean.get('id', None)

            if not pk:
                form.save()
            else:
                disco = get_object_or_404(Disco, pk=pk)
                disco.titulo = form_clean.get('titulo', '')
                disco.genero = form_clean.get('genero', '')
                disco.cantor = form_clean.get('cantor', '')
                disco.ano_lancamento = form_clean.get('ano_lancamento', '')
                disco.valor = form_clean.get('valor', '')

                disco.save()

            return HttpResponseRedirect(reverse('loja:index'))
    else:
        form = DiscoForm()

    return render(request, 'loja/cadastrar.html', {'form': form})


def editar(request, pk):
    disco = get_object_or_404(Disco, pk=pk)
    form = DiscoForm(instance=disco)

    return render(request, 'loja/alterar.html', {'form': form})


def remover(request, pk):
    disco = get_object_or_404(Disco, pk=pk)
    disco.delete()

    return HttpResponseRedirect(reverse('loja:index'))


def pesquisar(request):
    if request.method == 'POST':
        search_by = request.POST.get('search_by')
        query = request.POST.get('item')
        preco_min = request.POST.get('minimo', 0)
        preco_max = request.POST.get('maximo', 0)

        if search_by == 'titulo':
            discos = Disco.objects.filter(valor__gte=preco_min, valor__lte=preco_max, titulo=query).order_by('-valor')
        elif search_by == 'genero':
            discos = Disco.objects.filter(valor__gte=preco_min, valor__lte=preco_max, genero__nome=query).order_by('-valor')
        elif search_by == 'cantor':
            discos = Disco.objects.filter(valor__gte=preco_min, valor__lte=preco_max, cantor__nome=query).order_by('-valor')

        if not query:
            discos = Disco.objects.filter(valor__gte=preco_min, valor__lte=preco_max).order_by('-valor')

    return render(request, 'loja/index.html', {'list_discos': discos})
