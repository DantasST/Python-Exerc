#analisando nomes posições
print('\n**EXERCICIO 27**\n')
nome = str(input('Digite o nome completo: ')).strip()
print('O nome digitado é {}'.format(nome))
n = nome.split()
print('Primeiro nome: {}'.format(n[0]))
print('Último nome: {}'.format(n[len(n)-1]))
