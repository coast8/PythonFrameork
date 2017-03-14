"""
	construindo a app de usuarios de nosso sistema
"""

'a aplicação sera customizada totalmento, foi apagado o banco da aplicação'

obs: devem ser definadas configurações no settings
	para efetuar o login de usuarios

obs : nos urls_principal devem ser importados a views do django -->login e logout
	from django.contrib.auth.views import login, logout





**passos 

	criar o models
	ajustar o admin
	forms para ciar formulario


	obs: o django ja usa os campos padrao do propio django
	password1 e password2, essas senhas criptografadas e feitas as verificaçẽos 
	entao nao foram customizados nomodelo mais como ja existem foram declaradas no admin.



	bachends.py
	esse eh o arquivo para autenticacao e precisar de declarado no settings
	estamos usando o backends para pada autenticar de mais de uma maneira 
	usando o campo usuario e o campo email.