"""
27- Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M=H*10000, sendo M a área em metros quadrados e H
a área em hectares.
"""

print(f'\nDigite um valor de área em hectares para ser convertido para metros quadrados: \n')

hectares = input()

try:

    hectares = float(hectares)
    print(f'\n"{hectares} hectares" é equivalente a: {hectares*10000} metros quadrados.')

except ValueError:

    print(f'''
    "{hectares}" não é um número.
    Somente números são aceitos, inteiros ou reais.
    Feche o programa e tente novamente.''')
