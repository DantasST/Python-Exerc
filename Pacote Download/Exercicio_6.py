#Dobro, triplo e raiz quadrada
print('**EXERCICIO 6**\n')
num = int(input('Digite um número inteiro: '))
d = num*2
t = num*3
rq = num**(1/2)
print('Numero digitado: {}\nDobro: {}\nTriplo: {}\nRaiz Quadrada: {:.2f}\n '.format(num,d,t,rq))
#pode colocar os calculos dentro do format, assim nao ocupa memoria de variaveis