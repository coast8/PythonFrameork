d = float(input('Distância em km: '))
v = float(input('Velocidade média em km/h: '))
t = d / v

# este marcador vai mostrar apenas 1 casa decimal
# %.1f = marcador com uma casa decimal
# %.2f = marcador com duas casas decimais
print ('Tempo aproximado em horas: %.1f' %t)
