#sorteio nomes lista
import random
print('\n**EXERCICIO 20**\n')
nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))
print('A sequencia de apresentação é: ',random.sample([nome1, nome2, nome3, nome4], k=4))

