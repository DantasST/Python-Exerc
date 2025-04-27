#valor viagem
print('\n**EXERCICIO 31**\n')
dist = int(input('Qual a distância da viagem em Km/h: '))
if dist <= 200:
    print('Não ultrapassou 200km/h\n portanto o preço da passagem será R$ {:.2f}'.format(dist*0.50))
else:
    print('Ultrapassou 200km/h\n portanto o preço da passagem será R$ {:.2f}'.format(dist*0.45))