"""
19- Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. A
fórmula de conversão é: M = L/1000, sendo L o volume em litros e m o volume em metros
cúbicos.
"""

print(f'\nDigite um valor de volume em litros para ser convertido em metros cúbicos:\n')

litros = input()

try:

    litros = float(litros)
    print(f'\n"{litros} litros" é equivalente a: {litros/1000} m³')

except ValueError:

    print(f'''
    "{litros}" não é um número.
    Somente números são aceitos, inteiros ou reais.
    Feche o programa e tente novamente.''')
