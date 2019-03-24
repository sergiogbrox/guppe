"""
20- Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula
de conversão é: L = K/0,45 sendo K a massa em quilogramas e L a massa em libras.
"""

print(f'\nDigite um valor de massa em quilogramas para ser convertido em libras: \n')

quilogramas = input()

try:

    quilogramas = float(quilogramas)
    print(f'\n"{quilogramas} quilogramas" é equivalente a: {quilogramas/0.45} libras.')

except ValueError:

    print(f'''
    "{quilogramas}" não é um número.
    Somente números são aceitos, reais ou inteiros.
    Feche o programa e tente novamente.''')
