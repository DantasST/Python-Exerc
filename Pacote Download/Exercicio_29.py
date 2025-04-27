#velocidade do carro
print('\n**EXERCICIO 29**\n')
veloc = int(input('Informe a velocidade do carro: '))

if veloc>80:
    acima =veloc-80
    print('Limite de 80km/h, você ultrapassou {} km/h'.format(veloc-80))
    print('Multa de R$ 7.00 por Km/h ultrapassado')
    print('Será multado em R$ {:.2f}'.format(acima*7))
else:
    print('Voce nao será multado')


