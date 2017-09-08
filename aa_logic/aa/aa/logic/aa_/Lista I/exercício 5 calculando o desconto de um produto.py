m = float(input('Preço da mercadoria: '))
p = float(input('Porcentagem de desconto: '))
desconto = m * p / 100
novo = m - desconto

# vamos usa o conceito conhecido como marcadores
# a porcetagem são marcadores
# existem tres tipos de marcadores
#	%s = string  
#	%d = numeros decimais
#	%f = para nuros flutuantes (float)
print('Desconto: R$ %.2f' %desconto)
print('Preço a pagar: R$ %.2f' %novo)
