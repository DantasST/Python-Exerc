#aumento salario
print('\n**EXERCICIO 34**\n')
salario = float(input("Qual o salario do funcionário: R$ "))
if salario > 1250.00:
    print('Aumento de 10%, atualização de salario: R$ {:.2f}'.format((salario*0.1)+salario))
else:
    print('Aumento de 15%, atualização de salario: R$ {:.2f}'.format((salario*0.15)+salario))