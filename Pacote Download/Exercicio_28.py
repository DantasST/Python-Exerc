#joguinho de pensar
print('\n**EXERCICIO 28**\n')
from random import randint # sorteia numeros
from time import sleep #tempo de espera
pc = randint(0,5)
print('De 0 a 5, adivinhe qual numero o PC pensou')
#print('numero foi {}'.format(pc)) = sorteia o numero
num = int(input('O numero foi: '))
print('Processando....')
sleep(5)
#print('Voce acertou' if num==pc else 'Voce errou')
if num==pc:
    print('Voce acertou')
else:
    print('Voce errou')

