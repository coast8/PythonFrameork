from django.shortcuts import render
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import get_user_model


User = get_user_model()

def index(request):
	return render(request, 'index.html')


class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('index')


register = RegisterView.as_view()
