"""Django e MYSQL"""




A primeira alteração em nosso projeto que precisamos realizar é no arquivo 
  connectedin/connectedin/settings.py


	# connectedin/connectedin/settings.py
	# código anterior comentado

	DATABASES = {
	    'default': {
	        'ENGINE': 'mysql_cymysql', 
	        'NAME': 'connectedin',
	        'USER': 'root',
	        'PASSWORD': '',
	        'HOST': 'localhost', 
	        'PORT': '3306',
	    }
	}

	# código posterior comentado


	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	        'NAME': 'pythontest',
	        'USER': 'root',
	        'PASSWORD': '',
	        'HOST': 'localhost',
	        'PORT': '5432',
    	}
	}

Esta configuração assume que no MYSQL há um banco criado chamado connectedin, 
 o usuário root e a senha em branco. Será que isso é suficiente? Ainda não. 
 Estamos usando a engine django.db.backends.mysql que não vem por padrão no Django, 
 precisamos instalá-la. 

 	#############################################
 		$ pip3 install cymysql
		$ pip3 install django-cymysql
 	#############################################



Depois de baixado, precisamos aplicar nossas migrations em nosso banco connectedin 
 através da instrução migrate:

 	#############################################
 		python manager.py migrate
 	#############################################


O comando demorará alguns segundos, mas será o suficiente para subirmos já a nossa aplicação:

	#############################################
 		python manager.py runserver
 	#############################################