"""
6- Leia uma temperatura em graus Celsius e apresente-a convertida dem graus Fahrenheit.
A fórmula de conversão é: F = C*(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

print("\n Digite uma temperatura em graus Celsius para ser convertida em graus Fahrenheit.")

celsius = input()

try:
    print(f'''\n"{celsius}" graus Celsius é equivalente a "{float(celsius) * (9.0 / 5.0) + 32.0}" graus Fahrenheit.''')

except ValueError:
    print(f'''
    "{celsius}" não é um numero.
    Somente numeros são aceitos, inteiros ou reais.''')
