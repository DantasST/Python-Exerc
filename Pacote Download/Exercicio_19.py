#sorteio nomes
import random
print('\n**EXERCICIO 19**\n')
nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))
#random.choice([nome1, nome2, nome3, nome4])
print('O aluno sorteado é ',(random.choice([nome1, nome2, nome3, nome4])))
