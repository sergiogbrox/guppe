"""
18- Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. A
fórmula de conversão é: L = 1000*M, sendo L o volume em lítros e M o volume em
metros cúbicos.
"""

print(f'\nDigite um valor de volume em metros cúbicos para ser convertido para litros: \n')

cubicos = input()

try:

    cubicos = float(cubicos)
    print(f'\n"{cubicos}" m³ é equivalente a: {1000*cubicos} litros')

except ValueError:

    print(f'''
    "{cubicos}" não é um número.
    Somente números são aceitos, inteiros ou reais.
    Feche o programa e tente novamente''')
