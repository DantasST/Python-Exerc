#analisando triangulos
print('\n**EXERCICIO 35**\n')
r1 = float(input('Digite primeiro segmento: '))
r2 = float(input('Digite segundo segmento: '))
r3 = float(input('Digite terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triâgulo!')
else:
    print('Os segmentos acima não podem formar triângulo!')
