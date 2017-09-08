
# Setup Django, Apache2, Python Tools, and mod_wsgi on Debian Linux Systems (Debian Version 8.6 & Up)
sudo apt-get update

sudo apt-get upgrade

sudo apt-get install python-pip python-virtualenv python-setuptools python-dev build-essential


sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3 
sudo apt-get install libapache2-mod-wsgi # if using Python2






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









#########################################
#   Start Virtualenv & Django Project   #
#########################################

sudo pip install virtualenv 

cd /var/www

mkdir venv && cd venv

virtualenv -p python3 .

source bin/activate

python --version #should return Python 3.4

pip install django==1.10.3

mkdir src && cd src

django-admin.py startproject cfehome .

python manage.py migrate

python manage.py createsuperuser 









###############################################
#     Setup Static & Media Root directories   #
###############################################
cd /var/www

mkdir static-root && mkdir media-root











#####################
#      Open         #
#####################

# sudo nano /etc/apache2/sites-available/000-default.conf
<VirtualHost *:80>

    ServerName localhost
    ServerAdmin webmaster@localhost

    Alias /static /var/www/static-root
    <Directory /var/www/static-root>
       Require all granted
     </Directory>

    Alias /media /var/www/media-root
    <Directory /var/www/media-root>
       Require all granted
    </Directory>

    <Directory /var/www/venv>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess cfehome python-path=/var/www/venv/:/var/www/venv/lib/python3.5/site-packages
    WSGIProcessGroup cfehome
    WSGIScriptAlias / /var/www/venv/cfehome/wsgi.py


    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>














##########################################################
#     Add User Permissions (to modify sqlite3 Database)  #
##########################################################
sudo adduser $USER www-data
sudo chown www-data:www-data /var/www/venv/src    
sudo chown www-data:www-data /var/www/venv/src/db.sqlite3
sudo chmod -R 775 /var/www/venv/







######################################
#    Start, Stop, Restart Apache2    #
######################################
# Restart in two different ways:
sudo apachectl restart
sudo service apache2 restart


# Start Apache in two different ways:
sudo apachectl start
sudo service apache2 start

# Stop Apache in two different ways:
sudo apachectl stop
sudo service apache2 stop











####################################################################
#   Setup Domain Name DNS records: Add your server's ip_address    #
####################################################################
Type    Host                    Answer      TTL
A   www.yourdomain.com      45.79.183.218   300
A   blog.yourdomain.com     45.79.183.218   300








################################################
#  Add Any/All Hosts to Django Settings:       #
################################################
ALLOWED_HOSTS = ['45.79.183.218', 'www.yourdomain.com', 'blog.yourdomain.com']

#Add Static + Media Settings

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/static-root/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/media-root/'



# Restart Apache for finish





# FONTE:
    https://github.com/codingforentrepreneurs/Guides/blob/master/all/Debian_Install_Django_Apache2.md