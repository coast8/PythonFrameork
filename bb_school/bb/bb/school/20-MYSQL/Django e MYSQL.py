


# settings.py

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql_cymysql', 
	        'NAME': 'connectedin',
	        'USER': 'root',
	        'PASSWORD': '',
	        'HOST': 'localhost', 
	        'PORT': '3306',
	    }
	}


# Esta configuração assume que no MYSQL há um banco criado chamado connectedin, 
# o usuário root e a senha em branco. Será que isso é suficiente? Ainda não. 
# Estamos usando a engine django.db.backends.mysql que não vem por padrão no Django, 
# precisamos instalá-la. 

 	#############################################
 		$ pip3 install cymysql
		$ pip3 install django-cymysql
 	#############################################
