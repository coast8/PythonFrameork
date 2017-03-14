#modelos de views

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['form'] = form
    context['course'] = course
    template_name = 'courses/details.html'
    return render(request, template_name, context)


 '




from .forms import ContatoForm
from .forms import ClienteForm
from .models import Cliente

def contatos(request):
	if request.method == 'POST':
		contato_form = ContatoForm(request.POST)

		if contato_form.is_valid():
			user = contato_form.save()
			user.save()
			return redirect('core:sucesso_usuario')
		else:
			print(contato_form.errors)
	else:
		contato_form = ContatoForm()

	return render(request, 'contatos.html',\
		{'contato_form': contato_form})



def cadastro(request):
	if request.method == 'POST':
		form_cliente = ClienteForm(request.POST)

		if form_cliente.is_valid():
			novoCliente = form_cliente.save()
			novoCliente.save()
			return redirect('core:sucesso_cliente')
		else:
			print(form_cliente.errors)
	else:
		form_cliente = ClienteForm() 
	return render(request, 'core/cadastro.html', {'form_cliente': form_cliente})
