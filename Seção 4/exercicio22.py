"""
22- Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula
de conversão é: M = 0,91*J, sendo J o comprimento em jardas e M o comprimento
em metros.
"""

print(f'\nDigite um valor de comprimento em jardas para ser convertido para metros: \n')

jardas = input()

try:

    jardas = float(jardas)
    print(f'\n"{jardas} jardas" é equivalente a: {0.91*jardas} metros.')

except ValueError:

    print(f'''
    "{jardas}" não é um número.
    Somente números são aceitos.
    Feche o programa e tente novamente.''')
