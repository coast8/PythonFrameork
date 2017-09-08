
# Setup Django, Apache2, Python Tools, and mod_wsgi on Debian Linux Systems (Debian Version 8.6 & Up)
sudo apt-get update

sudo apt-get upgrade

sudo apt-get install python-pip python-virtualenv python-setuptools python-dev build-essential


sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3 
sudo apt-get install libapache2-mod-wsgi # if using Python2
#########################################################################################################





#######################################
# problemas com o apache  ou WSGI     #
#######################################

# remove o apache
sudo apt-get purge apache2

# reinstala o apache novamente
sudo apt-get install apache2

# removendo o wsgi mod-wsgi
sudo apt-get remove --purge libapache2-mod-wsgi

# instalando novamente
sudo apt-get install libapache2-mod-wsgi
sudo a2enmod wsgi #ativando
sudo service apache2 restart #reiniciando
#########################################################################################################




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
#########################################################################################################




# ativando o virtual-host
a2ensite eva2.conf

# restartando o apache
sudo service apache2 reload
	ou
sudo service apache2 restart

#########################################################################################################







# obs -> 
#	devem ser configuradas no settings.py da app as configurações de media e static


	# para os arquivos staticos
	STATIC_URL = '/static/'
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')

	# para os arquivos de media
#########################################################################################################
