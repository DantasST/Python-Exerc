#numero menor e maior
print('\n**EXERCICIO 33**\n')

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
        maior = b
if c > a and c > b:
        maior = c
print('O menor numero é: {}'.format(menor))
print('O maior numero é: {}'.format(maior))
