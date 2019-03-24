"""
9- Leia uma temperatura em graus Ceusius e apresente-a convertida em graus Kelvin. A
fórmula de conversão é:  K = C + 273.15, sendo C a temperatura em Ceusius e K a
temperatura em Kelvin.
"""

print('\nDigite uma temperatura Celsius para ser convertida para graus Kelvin:\n')

celsius = input()

try:
    celsius = float(celsius)
    print(f'\n"{celsius}" é equivalente a: \n {celsius + 273.15}')

except ValueError:
    print(f'''
    "{celsius}" não é um numero.
    Somente numeros são aceitos, inteiros ou reais.
    Feche o programa e tente novamente.''')
