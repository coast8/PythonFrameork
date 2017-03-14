#ENTRAMOS AGORA NO MODULO DE SISTEMAS DE USUARIOS




' fazer login no sistema e logaut
passos:
	1 - deve ser creado um app de contas

	2 - no url da app contas deves usar o a view do django ja pronta
		e essa url deve ter um parametro a mais que eh o do template do login. 

		#view do Djngo para o login
		#view do Djngo para o logout
			django.contrib.auth.views.login
			django.contrib.auth.views.logout
		

	3 -  hora de criar o template de login.
			obs: no template base deve if para verificar se o usuario estar logado
				se logado vai mostrar SAIR e DASBOARD senao mostra ENTRA 

	4 - devemos ir agora do arquivo settings definir a navegação do usuario logado. 
		#Auth


'criando outros usuario
passos:
	1-criar o url 
	2-criar a view 
	3-criar a template 





'painel do usuario
passos:
	1- deve ser criado o url do dashboard--gerenciamento de conta 

	2- criar a view

	3- usar o decaration sobre a view do DASBOARD para verificar se o usuario
		estar realmente logado, senao ele redireciona para seting que aponta para 
		o longin.


	4 - criar template de DASBOARD.


'criando ações do usuario
passos:
	1-edição de conta
	2-alterar a senha
	3-permiçoes de usuarios 
	4-defina nova senha