"""
13- Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de
conversão é: M=K/1.61, sendo K a distância em quilômetros e M em milhas.
"""

print(f'Digite uma distãncia em quilômetros para ser convertida em milhas: ')

quilometros = input()

try:

    quilometros = float(quilometros)
    print(f'''
    "{quilometros} quilômetros" é equivalente a: {quilometros/1.61} milhas.''')

except ValueError:

    print(f'''
    "{quilometros}" não é um número.
    Somente numeros são aceitos, reais ou inteiros.
    Feche o programa e tente novamente.''')
