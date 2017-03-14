# aplicação de usuarios 



# estas views usam a urls principal
'entrar, sair e cadrastre-se'
# login e logout recebemn parametras a mais no urls pois ja usam a 
# view padrao do django e precisa indicar o template.



# view de cadrastro usa ClassbasedView -> usa o modelo e formuçlarios padrão do Django 
	
	from django.contrib.auth import get_user_model # models

	from django.contrib.auth.forms import UserCreationForm #formulario


"""
	não foi preciso modelar nada pois já usamos tudo pronto do django
	models e forms 
"""  

