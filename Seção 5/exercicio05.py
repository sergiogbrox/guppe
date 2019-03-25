numero = int(input('Digite um numero:\n'))

if numero % 2 == 0 and numero != 0:
    print('o número é par!')
elif numero == 0:
    print('o número é neutro!')
else:
    print('o número é inpar!')
