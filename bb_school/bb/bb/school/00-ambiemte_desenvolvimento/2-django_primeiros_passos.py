
## entrando no ambiente virtual
	source bin/activate


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



## criando tabelas no banco de dados
	python manage.py migrate
	
## mapeando as mudanças
	python manage.py makemigrations

## cria o super usuario para admin
	python manage.py createsuperuser 

# rodando o servidor
	python manage.py runserver
