"""
35- Sejam 'a' e 'b' os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa= raiz_quadrada de a²+b². Faça um programa que receba os valores de 'a' e 'b' e calcule
o valor da hipotenusa através da equação. Imprima o resultado dessa operação.
"""

print(f'\nCalculadora de Hipotenusa.')

a = input('Digite o valor do primeiro cateto: ')
b = input('Digite o valor do segundo cateto: ')

try:
    a = float(a)
    b = float(b)
    print(f'\nO valor da hipotenusa é {(a**2+b**2)**0.5}.')

except ValueError:

    print('Somente números são aceitos. Feche o programa e tente novamente.')
