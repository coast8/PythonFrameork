# Ao tentar criar múltiplos virtual hosts no XAMPP eu sempre tinha o mesmo problema: 
# qualquer um dos domínios que eu utilizasse, o Apache redirecionava apenas para 
# a mesma pasta.

# O que acontece é que qualquer erro que seja encontrado em um arquivo, 
# o Apache utiliza a pasta do primeiro Virtual Host como padrão. 
# Então para que isso não ocorra, siga este passo-a-passo:


# Edite seu arquivos de hosts 
127.0.0.1   dominio1.com.br
127.0.0.1   www.dominio1.com.br
127.0.0.1   dominio2.com.br
127.0.0.1   www.dominio2.com.br


















# Virtual Hosts
#
# Required modules: mod_log_config
 
# If you want to maintain multiple domains/hostnames on your
# machine you can setup VirtualHost containers for them. Most configurations
# use only name-based virtual hosts so the server doesn't need to worry about
# IP addresses. This is indicated by the asterisks in the directives below.
#
# Please see the documentation at 
# <URL:http://httpd.apache.org/docs/2.4/vhosts/>
# for further details before you try to setup virtual hosts.
#
# You may use the command line option '-S' to verify your virtual host
# configuration.
 
#
# Use name-based virtual hosting.
#
 
NameVirtualHost 127.0.0.1:80
 
#
# VirtualHost example:
# Almost any Apache directive may go into a VirtualHost container.
# The first VirtualHost section is used for all requests that do not
# match a ##ServerName or ##ServerAlias in any <VirtualHost> block.
#
 
<VirtualHost *:80>
    ServerName default
    DocumentRoot "C:\xampp\htdocs"
    ErrorLog "logs/default-error.log"
    CustomLog "logs/default-access.log" common
    <Directory "C:\xampp\htdocs">
        DirectoryIndex index.php index.html index.htm
        AllowOverride All
        Order allow,deny
        Allow from all
    </Directory>
</VirtualHost>
 
<VirtualHost *:80>
    ServerName dominio1.com.br
    ServerAlias www.dominio1.com.br
    DocumentRoot "C:\xampp\htdocs\dominio1.com.br"
    ErrorLog "logs/dominio1-error.log"
    CustomLog "logs/dominio1-access.log" common
    <Directory "C:\xampp\htdocs\dominio1.com.br">
        DirectoryIndex index.php index.html index.htm
        AllowOverride All
        Order allow,deny
        Allow from all
    </Directory>
</VirtualHost>
 
<VirtualHost *:80>
    ServerName dominio2.com.br
    ServerAlias www.dominio2.com.br
    DocumentRoot "C:\xampp\htdocs\dominio2.com.br"
    ErrorLog "logs/dominio2-error.log"
    CustomLog "logs/dominio2-access.log" common
    <Directory "C:\xampp\htdocs\dominio2.com.br">
        DirectoryIndex index.php index.html index.htm
        AllowOverride All
        Order allow,deny
        Allow from all
    </Directory>
</VirtualHost>