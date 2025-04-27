#seno, cosseno e tangente
from math import sin, cos, tan, radians
print('\n**EXERCICIO 18**\n')
ang = float(input('Digite o angulo: '))
print(f'O angulo digitado tem:\nseno de {sin(radians(ang)):.2f}\ncosseno de {cos(radians(ang)):.2f}\ntangente de {tan(radians(ang)):.2f}')
