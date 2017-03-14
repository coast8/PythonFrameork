
from django.shortcuts import render

from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Course

# Create your views here.
#pagina home, primeira pagina criada
def home(request):
	

	#listando todos os Course de models
	courses = Course.objects.all()
	template_name = 'index.html'
	context = {
        'courses': courses
    }
	return render(request, template_name, context)