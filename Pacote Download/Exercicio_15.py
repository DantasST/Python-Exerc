#aluguel de carros
print('\n**EXERCICIO 15**\n')
dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Qual a quantidade de Km percorrido: '))
print(f'O valor total a pagar é R$ {((dias*60)+(km*0.15)):.2f}')