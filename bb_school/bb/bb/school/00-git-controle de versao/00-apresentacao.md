## site que contem as linhas de comando do GITHUB
	try.github.io











--------------------------------------------------------------------
#######################################################
#                       fandre                        #
#######################################################

###############
# instalação  #
###############
	##instalando o git
apt-get install git

	## procedimentos de identificação
git config --global user.name nome_usuario
git config --global user.email email_usuario





################
# manipulação  #
################


	git init 	#mapear um diretorio
	git add . 	#todas as mudanças no diretorio
	git status	#
	git commit -m "mensagem sobre alteração"			#
	git remote add origin url-do-diretorio-github-ssh 	#
	git push origin master


	git add . 	#todas as mudanças no diretorio
	git status	#
	git commit -m "mensagem sobre alteração"
	git push origin master


	git clone origin url-do-diretorio-github-ssh






















--------------------------------------------------------------------
#######################################################
#                       casa do codigo                   #
#######################################################



	##  TRANSFORMA O DIRETORIO ATUAL EM UM REPOSITORIO DO GIT
git init
	## Deverá aparecer uma mensagem semelhante à seguinte:
Initialized empty Git repository in /home/fulano/citacoes/.git/


	## RASTREANDO ARQUIVO
git add filmes.txt


	## VERIFICANDO OS ARQUIVOS QUE ESTÃO SENDO RASTREADOS
git status


	##gravarmos as mudanças no repositório
git commit -m "Arquivo inicial de citacoes"


	##Alterando o arquivo, Insira mais uma linha no arquivo filmes.txt , com o conteúdo:
	## "Hasta la vista, baby." (Exterminador do Futuro 2)
git status
git add filmes.txt
git commit -m "Inserindo nova citacao"


	## verificar o histórico das alterações gravadas no repositório
git log


	## Apontando seu projeto para o GitHub
git remote add origin https://github.com/SmythyCosta/citacoes.git


	## Enviando as alterações para o GitHub
git push origin master
	## Forneça seu usuário e senha do GitHub quando solicitado.

	## Rastreando vários arquivos
git add .


