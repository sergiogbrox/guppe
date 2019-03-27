numero = input('Digite um número inteiro maior que zero: ')

if int(numero) > 0:
    print(sum(int(i)for i in numero))
else:
    print('inválido')
