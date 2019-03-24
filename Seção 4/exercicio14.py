"""
14- Leia um ângulo em graus e arpresente-o convertido em radianos. A fórmula de conversão
é: R=G*pi/180, sendo G o ângulo em graus e R em radianos e pi = 3.14.
"""

print(f'\nDigite um ângulo em graus para ser convertido em radianos: ')

graus = input()

try:

    graus = float(graus)
    print(f'''
    "{graus} graus" é equivalente a: {graus*3.14/180}''')

except ValueError:

    print(f'''
    "{graus}" não é um numero.
    Somente numeros são aceitos.
    Feche o programa e tente novamente.''')
