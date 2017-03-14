## p a p.

# domino do host
sudo vim /etc/hosts
	'127.0.0.1   djangowsgi.com'

# criando uma virtualhos
vim /etc/apache2/sites-available/eva2.conf

	## arquivo que aponta para a aplicação rodar em modo de prodoução
	#################      begin           #######################################################
	<VirtualHost *:80>

	    ServerName eva2.com
	    ServerAlias eva2.com

	    WSGIScriptAlias / /home/tatu/eva2/meusite/meusite/wsgi.py
	    WSGIDaemonProcess eva2.com python-path=/home/tatu/eva2/meusite:/home/tatu/eva2/lib/python3.4/site-packages
	    WSGIProcessGroup eva2.com

	    ErrorLog /home/tatu/eva2/meusite/error.log
	    DocumentRoot /home/tatu/eva2/meusite


	    <Directory /home/tatu/eva2/meusite/meusite>
	      <Files wsgi.py>
	        Require all granted
	      </Files>

	    </Directory>


	    Alias /static /home/tatu/eva2/meusite/static
	    Alias /media /home/tatu/eva2/meusite/media


	    <Directory /home/tatu/eva2/meusite/static>
	      Require all granted

	    </Directory>

	    <Directory /home/tatu/eva2/meusite/meusite/media>
	      Require all granted
	    </Directory>

	</VirtualHost>
	###################       end            #######################################################




# ativando o virtual-host
a2ensite eva2.conf



# restartando o apache
sudo service apache2 reload
	ou
sudo service apache2 restart




# obs -> 
#	devem ser configuradas no settings.py da app as configurações de media e static


	# para os arquivos staticos
	STATIC_URL = '/static/'
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')

	# para os arquivos de media
	