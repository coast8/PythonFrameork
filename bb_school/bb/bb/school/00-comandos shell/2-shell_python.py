## entrando no ambiente virtual
	source bin/activate



## deve estar dentro do ambiemte virtual, o virtual-env

## esse comando criara o projeto e as pastas com seus diretrios.
##  criando o projeto que se chamara agenda.

	django-admin startproject agenda 

## criando app.
## deve estar dentro da agenda
	django-admin startapp contatos
		ou
	../manage.py startapp contatos

## devemos registrar a nossos app
	settigs.py  → 
		
		INSTALLED_APPS = 
			'agenda.core', 
    			'agenda.contatos',
		
		LANGUAGE_CODE = 'pt-br'

##criando sql lite
	python manage.py migrate
	


## depois que criar novas app deve fazer a migração
## criar um arquivo 0001_inital.py
## deve estar sempre no diretorio /agenda
	../manage.py makemigrations


	syncdb = Cria tabelas no banco de dados
	python manage.py syncdb


## cria o super usuario para admin
	../manage.py createsuperuser
	
##logo em seguida pergunta se quer criar um super administrador
## sim e cria:  
	login = admin
	e-mail = 
	senha = 


## na primeira vez que rodar o servidor deve ser feita essa sequencia
## comando para rodar o servidor python
	1    -	 ../manage.py runserver
		
	2    -	../manage.py migrate

	3    -	 ./manage.py runserver

## digita no navegador 
	localhost:8000
	127.0.0.1:8000/admin 