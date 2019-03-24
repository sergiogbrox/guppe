"""
47- Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
"""

try:

    numero = int(input('Digite um número inteiro de 4 digitos (de 1000 a 9999) para ser impresso um número por linha:'))

    if numero in range(1000, 10000):
        numero = str(numero)
        for index, value in enumerate(numero):
            print(value)

    else:

        print('Erro: Somente números inteiros de 4 dígitos são aceitos. Feche o programa e tente novamente.')

except ValueError:

    print('Erro: Somente números inteiros de 4 dígitos são aceitos. Feche o programa e tente novamente.')

