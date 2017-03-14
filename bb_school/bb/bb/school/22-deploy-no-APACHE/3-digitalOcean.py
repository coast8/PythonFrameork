documentation django deployment wsgi

###########################################################
#                         DEPLOY COM APACHE               #
###########################################################




###########################################################
#    configurações devem ser realizadas na maquina crua   #
###########################################################

# extenções em C, para fazer a compilação
apt-get install build-essential -y

# instalando o GIT
apt-get install git-core -y


# dependencias
################################################################
#    pacotes globais para que funcionem em todos os projetos   #
################################################################
apt-get install python-dev python-imaging python-mysqlbd python-virtualenv

apt-get install memcached

# criando o diretorio do deploy na raiz do sistema
/deploy


# criando o diretorio sub diretorios no deploy
/deploy/sites #codigo fonte dos sites em django, para clonar projeto
/deploy/virtualenvs #virtual env da app


# ctrabalhando no projeto
/deploy/virtualenvs #dentro desse diretorio
    # --system-site-packages, esse comando eh para usarmos os pacotes globais que foram instalados.
    virtualenv --system-site-packages mixincode #mixincode, criando esse virtual env.

    #ativa o ambiemte
    source mixincode/bin/activate

    # com o ambiemte ja ativado vamos voltar para o diretorio do git
    /deploy/sites/projeto #projeto eh o site ja tem que estar clonado
    pip install -r requirements.txt #vai instalar as dependencias do projeto

    #OBS O FREEZE EH O COMANDO QUE CRIA O requirements.txt
    pip freezer



################################################################
#                  configuraçoes do apache                     #
################################################################
#instalar o apache
apt-get install apache2

# para pegar o adaptador do wsgi
apt-cache search wsgi

# instalar o adaptador do wsgi
apt-get install libapache2-mod-wsgi


# verificar se estar funcionando o wsgi
ls /etc/apache2/mods-enabled
    
    nano wsgi.load #carrega o wsgi no apache

# define as configurações padroes do site que o apache vai exibir
vim /etc/apache2/sites-available/default.conf

# devemos criar nosso propioi default
mv default.conf eva2.conf

        <VirtualHost *:80>

        ServerName eva2.com
        ServerAlias eva2.com

        #primerio servimos os arquivos staticos e media
        Alias /static /home/tatu/eva2/meusite/static
        Alias /media /home/tatu/eva2/meusite/media


        <Directory /home/tatu/eva2/meusite/static>
          Require all granted

        </Directory>

        <Directory /home/tatu/eva2/meusite/meusite/media>
          Require all granted
        </Directory>


        #ao final as conf padroes
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


        

    </VirtualHost>



# ativando o virtual-host
a2ensite eva2.conf

# restartando o apache
sudo service apache2 reload
    ou
sudo service apache2 restart




# obs -> 
#   devem ser configuradas no settings.py da app as configurações de media e static


    # para os arquivos staticos
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    # para os arquivos de media


# mapear endereços IP para DNS
 vim /etc/hosts
    '127.0.0.1   meusite.com'

# subindo os arquivos staticos e de media
python .manage.py collectstatic  
































###########################################################
#                         DEPLOY COM nginx e guinicorn    #
###########################################################

# servidor para servir arquivos staticos e de media
apt-get install nginx
    
    /etc/init.d/nginx start #iniciando o servico

    127.0.0.1 #testando no navegador

# gunicorn, servidor 
apt-get install gunicorn

# rodando o projeto
gunicorn mixincode.wsgi:application -b 127.0.0.1:9001

# configurações semelhante ao ao apache
/etc/nginx/sites-available/ cp default mixincode

    nano mixincode#modificando o arquivo de configurações
    #################################################################################
        
        #http://docs.gunicorn.org/en/latest/deploy.html
        #passando o endereço do proxi reverso
        upstream app_server {
                # fail_timeout=0 means we always retry an upstream even if it failed
                # to return a good HTTP response

                # for UNIX domain socket setups
                #server unix:/tmp/gunicorn.sock fail_timeout=0;

                # for a TCP configuration
                server 127.0.0.1:9001 fail_timeout=0;
        }
        # **
        server {
                # if no Host match, close the connection to prevent host spoofing
                listen 80 default_server;
                return 444;
        }

        server {
                # use 'listen 80 deferred;' for Linux
                # use 'listen 80 accept_filter=httpready;' for FreeBSD
                listen 80;
                client_max_body_size 4G;

                # set the correct host(s) for your site
                server_name www.mixincode.com;

                keepalive_timeout 5;

                location /static/ {#static URl
                    alias /home/www/myhostname.com/static/;
                    expires 30d;
                }

                location /media/ {#media URl
                    alias /home/www/myhostname.com/media/;
                    expires 30d;
                }

                # path for static files
                #root /path/to/app/current/public;

                location / {
                  # checks for static file, if not found proxy to app
                  try_files $uri @proxy_to_app;
                }
        }

        location @proxy_to_app {
                  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                  # enable this if and only if you use HTTPS
                  # proxy_set_header X-Forwarded-Proto https;
                  proxy_set_header Host $http_host;
                  # we don't want nginx trying to do something clever with
                  # redirects, we set the Host: header above already.
                  proxy_redirect off;
                  proxy_pass http://gunicorn_server;
        }








# ativando o site nonginx
/etc/nginx/sites-enabled/mixincode #mixincode deve ser criado


/etc/init.d/nginx reload