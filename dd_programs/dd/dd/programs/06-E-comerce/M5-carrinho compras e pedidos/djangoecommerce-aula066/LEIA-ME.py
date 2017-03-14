"""
	P a P
"""


django.contrib.ssesion 
	trabalha com ssesion e cookie, fica salvo no banco de dados e 
	salva um dicionario de dados do usuario.

django.contrib.messege 
	sistema para imprimir mensagens. 

	existe um context_processes para app de mensagens



1- 'modelagem do carrinho de compras'
	chekout/models --> class CartItem


2- 'criando um template-para include'
	catalog/templates --> _pruduct.html

3- 'criando um manager'
	chekout/models --> class CartItemManager

4- 'adicionando produtos ao carrinho'
	chekout/views --> class CreateCartItemView 

5- 'formulario do carrinho'
	chekout/views --> class CartItemView

6- 'remoever item do formulario do carrinho, signals que ja um sistema do django'
	signals

7 - 'modelagem do pedido'
		chekout/models --> class Order
		chekout/models --> class OrderItem

8- 'finalizar comprar e criar pedido'


9- 'middleware --> captura as ações antes e depois'
	"""
		middleware precisa ser declarado no settings, existe mundças de middleware a partir da versao 1.10
		do django.
	"""
	