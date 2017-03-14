# entrando com o ano
a = int(input('Ano: '))
# processo lógico
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
  print ('Bissexto')
else:
  print ('Não é bissexto')
