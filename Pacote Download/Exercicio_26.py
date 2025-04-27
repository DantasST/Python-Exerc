#analisando frases posições
print('\n**EXERCICIO 26**\n')
frase = input('Digite a frase desejada: ').upper().strip()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('Primeira posição: {}'.format(frase.find('A')+1))
print('Ultima posição: {}'.format(frase.rfind('A')+1))