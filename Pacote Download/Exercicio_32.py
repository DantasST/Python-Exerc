#ano bissexto
print('\n**EXERCICIO 32**\n')
from datetime import date
ano = int(input('Descubra se um ano é bissexto: \n Para ano atual digite 0 \n Qual ano quer analisar: '))
if ano == 0:
    ano = date.today().year # data atual
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))