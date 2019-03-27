import math

numero = input('Digite um número positivo: ')

if int(numero) > 0:
    print(math.log(int(numero)))
else:
    print('invalido')
