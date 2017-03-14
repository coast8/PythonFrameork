__author__ = 'juniorlima'

from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView

from blog.models import Postagem
from design.models import Portifolio, Tipo
from configs.models import Configuracao, Servico, Habilidade

class HomePageView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_posts'] = Postagem.objects.all()[:5]
        context['latest_portifolio'] = Portifolio.objects.filter(publicar=True, destaque=True).order_by('-my_order')[:32]
        context['latest_config'] = Configuracao.objects.latest('id')
        context['latest_servico'] = Servico.objects.filter(publicar=True)
        context['latest_habilidade'] = Habilidade.objects.filter(publicar=True)
        context['tipos'] = Tipo.objects.filter(publicar=True)
        return context

class PolifolioListView(ListView):
    model = Portifolio
    def get_context_data(self, **kwargs):
        context = super(PolifolioListView, self).get_context_data(**kwargs)
        context['latest_portifolio'] = Portifolio.objects.filter(publicar=True, destaque=True).order_by('-id')
        context['tipos_list'] = Tipo.objects.all()[:5]
        return context

class TipoListView(ListView):
    model = Tipo
    slug_field = 'slug'

class PostDetailView(DetailView):
    model = Postagem
    slug_field = 'slug'