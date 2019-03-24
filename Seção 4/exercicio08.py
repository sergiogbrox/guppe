"""
8- Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Ceusius e K a
temperatura em Kelvin.
"""
print("\nDigite uma tenmperatura em graus Kelvin para ser convertida para graus Celsius:\n")

kelvin = input()

try:
    kelvin = float(kelvin)
    print(f'\n "{kelvin}" graus Kelvin é equivalente a:\n {kelvin - 273.15} graus Celsius.')

except ValueError:
    print(f'''
    "{kelvin}" não é um numero.
    Somente numeros são aceitos, inteiros ou reais.
    Feche o programa e tente novamente.''')
