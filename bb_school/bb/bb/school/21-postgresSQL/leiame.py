


## codigo para conexao com db

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


## lib que deve ser instalada
pip install psycopg2