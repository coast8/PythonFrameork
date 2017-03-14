from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CampanhaForm

# Create your views here.

#@login_required(login_url='/login/')
#def dashboard(request):
#	return render(request, 'campanha/dashboard.html')

@login_required(login_url='/login/')
def dashboard(request):
	return render(request, 'campanha/dashboard.html')

def add_campanha(request):
	if request.method == 'POST':
		form_campanha = CampanhaForm(request.POST, request.FILES)
		if form_campanha.is_valid():
			instance = Campanha(imagem=request.FILES['imagem'])
			instance.save()
			return redirect("campanha:sucesso")
		else:
			print(form_campanha.errors)
	else:
		form_campanha = CampanhaForm()
	return render(request, "campanha/add_campanha.html", {'form_campanha': form_campanha})