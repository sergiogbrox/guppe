"""
15- Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R*180/pi, sendo G o ângulo em graus e R em radianos e pi=3.14.
"""

print(f'\nDigite um ângulo em radianos para ser convertido para graus: ')

angulo = input()

try:

    angulo = float(angulo)
    print(f'\n"{angulo} graus" é equivalente a: {angulo * 3.14 / 180} radianos')

except ValueError:

    print(f'''
    "{angulo}" não é um numero.
    Somente numeros são aceitos, reais ou inteiros.
    Feche o programa e tente novamente.''')
