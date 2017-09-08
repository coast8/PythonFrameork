
##############################################
#    instalando pacotes no servidor cru      #
##############################################

# compiladores de C e C++
	sudo apt-get install build-essential

# compiladores de C e C++
	sudo apt-get install python-dev

# python integração com postgresql
	sudo apt-get install python-psycopg2 

# criar ambiente isolados
	sudo apt-get install python-virtualenv

# git 
	sudo apt-get install git-core



##############################################
#    instalando postgresql como db           #
##############################################

# postgresql
	sudo apt-get install postgresql 

	# entra nesse arquivo de configuração 
		nano /etc/postgresql/9.1/main/postgresql.conf
		#descomenta
			listen_addresses = 'localhost'

	#alterando a senha do usuario postgresql
		sudo -u postgresql psql template1

		ALTER USER postgres with encrypted password 'you_password';

	# entra nesse arquivo de configuração, para utilização de senhas MD5
		nano /etc/postgresql/9.1/main/pg_hba.conf
			#altera a linha para ficar como a de baixo
				local all postgres md5 #peer

	# restartando o postgres
	sudo /etc/init.d/postgresql restart


# creando base de dados
	createdb -U postgres shortener
	createdb -U postgres sentry







##############################################
#    Servidor - instalando nginx             #
##############################################

# instalando
sudo apt-get install nginx

# restartando o servidor
sudo /etc/init.d/nginx restart














##############################################
#             aplicação                      #
##############################################

# criando diretorio
mkdir /deploy/

# dando permissao, deve-se checar o funcionamento desse comando
sudo chown vagrant:root /deploy/ -R

# entrando no diretorio
cd /deploy/

# criando subdiretorios
mkdir sites venvs

# entrando no diretorio
cd /venvs/

# criando um ambiente virtual de nome shortener
virtualenv --system-site-packages shortener

# criando um ambiente virtual de nome sentry
virtualenv --system-site-packages sentry

# ativando o ambiemte
source shortener/bin/activate

# navegando para o diretorio sites
cd /deploy/sites/

# clonando o projeto do git hub
git clone projeto

# dentro do projeto deves instalar as dependencias do projeto do requirements.txt
pip install -r requirements.txt

# testendo o projeto com o servidor de desenvolvimento
python manager.py runserver 0.0.0.0:8000

# criar as tabelas 
python manager.py migrate

# ajustar o settings para produção
DEBUG = False
ALLOWED_HOSTS = [ 'IP ou DOMINIO' ]



##############################################
#    Servidor - instalando gunicorn          #
##############################################

# instalando o gunicorn
apt-get install gunicorn

# rodando o servidor
gunicorn shortener.wsgi:application 




##############################################
#    Proxy Reverse - com Nginx               #
##############################################

# entrado no diretorio de configuraçao do nginx
cd /etc/nginx

# arquivos com sites default
cd /sites-available

#fazer uma copia do aquivo padrão
cp default encurtador

# estamos com dois arquivos ( default e encurtador)
# vamos agora editar o arquivo encurtador que é o arquivo do site.
nano encurtador



##################################################################
# colocando a mão no codigo editando o arquivo de configuração.  #
##################################################################

	upstream encutador_gunicorn {

	    # for a TCP configuration
	    server 127.0.0.1:9000 fail_timeout=0;

	  }

	server {
	    
	    listen 80;
	    client_max_body_size 4G;
	    server_name www.example.com;

	    keepalive_timeout 5;

	    location /static/ { 	# STATIC_URL
	      alias /deploy/sites/shortener/static/;
	      expires 30d;
	    }

	    location /media/ { 	# MEDIA_URL
	      alias /deploy/sites/shortener/media/;
	      expires 30d;
	    }

	    location / {
	      # checks for static file, if not found proxy to app
	      try_files $uri @proxy_to_app;
	    }

	    location @proxy_to_app {
	      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	      proxy_set_header Host $http_host;
	      proxy_redirect off;
	      proxy_pass http://encutador_gunicorn;
	    }


	  }


# navegado para esse diretorio
cd /etc/nginx/sites-enabled/

# criando linkin simbolico
sudo ln -s /etc/nginx/sites-available/encurtador

# listando os links( é para ter os dois links ( feault e apontador))
ls -la

# reiniciando o servidor 
sudo /etc/init.d/nginx reload

# rodando o servidor na porta que habilitamos no arquvo de configuração
gunicorn shortener.wsgi:application -b 127.0.0.1:9000




##############################################
#    Servindo os arquivos Staticos           #
##############################################

# navegado para esse diretorio
cd /etc/nginx/sites-enabled/encurtador

# estao abaixo os scripts mais ja colocamos no sites-enabled

		location /static/ { 	# STATIC_URL
	      alias /deploy/sites/shortener/static/;
	      expires 30d;
	    }

	    location /media/ { 	# MEDIA_URL
	      alias /deploy/sites/shortener/media/;
	      expires 30d;
	    }


# reiniciando o servidor 
sudo /etc/init.d/nginx reload


# comando para coletar os arquivos staticos
	

# confirma dando o yes
yes






#########################################
#    extras  - supervisor              #
########################################

# instalando o supervisor para da boot e monitorar as requisições do servidor
apt-get install supervisor

cd /etc/supervisor/

# esses arquivos serao lidos pelo supervison
cd conf.d/

# devemos criar esse arquivo 
nano gunicorn.conf

#configurando o arquivo de cima
[program:gunicorn-encurtador]
command=/deploy/venvs/shortener/bin/gunicorn shortener.wsgi:application -b 127.0.0.1:9000
directory=/deploy/sites/shortener
user=nobody
autostart=true
autorestart=true
redirect_stderr=true


# 
sudo etc/init.d/supervasior stop

sudo etc/init.d/supervasior start




# para ver processos
ps axf

sudo supervisorctl







##############################################
#   instalando o sentry                      #
##############################################

# ativando o ambiemte virtual
source /deploy/venvs/sentry/bin/activate

# instalando no ambiemte, programa para monitorar outras aplicações
pip install sentry








FONTES:
http://pythonclub.com.br/configurando-um-servidor-de-producao-para-aplicacoes-python.html




