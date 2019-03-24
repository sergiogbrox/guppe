"""
23- Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula
de conversão é: M = 0,91*J, sendo J o comprimento em jardas e M o comprimento em metros.
"""

print(f'\nDigite um valor de comprimento em metros para ser convertido para jardas: \n')

metros = input()

try:

    metros = float(metros)
    print(f'\n"{metros} metros" é equivalente a: {metros/0.91} jardas.')

except ValueError:

    print(f'''
    "{metros}" não é um número.
    Somente números são aceitos, reais ou inteiros.
    Feche o programa e tente novamente.''')
