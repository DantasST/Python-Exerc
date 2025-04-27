#Strings em diversos formatos
print('\n**EXERCICIO 22**\n')
nome = input('Digite o nome completo: ').strip()
print('Em Maiusculo: {}'.format(nome.upper()))
print('Em Minusculo: {}'.format(nome.lower()))
print('O nome possui {} letras'.format(len(nome)-nome.count(' ')))
#print('O primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
