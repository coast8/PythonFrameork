# Create your views here.
from django.views.generic.simple import direct_to_template

def teste(request):
    return "oi" #    assert False

def index(request):
    return direct_to_template(template="estoque/index.html")



