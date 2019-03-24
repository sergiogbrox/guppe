"""
46- Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:

NúmeroLido = 123
NúmeroGerado = 321
"""
try:
    numero = int(input('Digite um número inteiro de 3 digitos para ser invertido: '))

    if numero in range(100, 1000):
        numero = str(numero)
        print(numero[::-1])

    else:
        print('Erro: Somente números inteiros de 3 dígitos são aceitos. Feche o Programa e tente novamente. ')

except ValueError:

    print('Erro: Somente números inteiros de 3 dígitos são aceitos. Feche o Programa e tente novamente.')
