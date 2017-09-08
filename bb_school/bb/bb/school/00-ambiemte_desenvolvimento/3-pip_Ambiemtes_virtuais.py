
# pip é o ambiemte virtual para desenvolvimento em python.
# e nele podemos instalar softwres sem que estejam instalados 
# em nossa maquina principal.



# Qual versão do PIP devo usar?


# Python 2x e Python3x, normalmente você acaba tendo pip e pip3. A diferença é que pip instala 
# as bilbiotecas no Python 2 e pip3 instala as bilbiotecas no Python 3 ou no seu virtualenv.



###############################################
#    Python 3 montando ambiemtes virtuais     #
###############################################


	virtualenv -p /usr/bin/python3.4 meuambientevirtual
	
	cd meuambientevirtual

	source bin/activate

	
	## instalando o Django

		pip3 install django


	## interpretador do python, ja completa o codigo
		sudo apt-get install ipython





###############################################
#    Python 2 montando ambiemtes virtuais     #
###############################################


	virtualenv --system-site-packages meuambientevirtual

	source shortener/bin/activate


