"""
12- Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de
conversão é: K=1,61*M, sendo K a distancia em quilômetros e M em milhas.
"""


print('\nDigite uma distância em milhas para ser convertida em quilometros\n')

milhas = input()

try:

    milhas = float(milhas)

    print(f'''
    "{milhas} milhas" é equivalente a: {milhas * 3.6} quilômetros''')


except ValueError:

    print(f'''
    "{milhas}" não é um número.
    Somente numeros são aceitos, reais ou inteiros.
    Feche o programa e tente novamente.''')
