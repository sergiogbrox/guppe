"""
7- Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0 * (F - 32.0) / 9.0, sendo C a temperatura em Ceusius
e F a temperatura em Fahrenheit.
"""

print('\nDigite a temperatura em graus Fahrenheit para ser convertida para graus Ceusius.\n')

fahrenheit = input()

try:
    fahrenheit = float(fahrenheit)
    print(f'\n"{fahrenheit}" graus Fahrenheit é equivalente a: "{5.0 * (fahrenheit - 32.0) / 9.0}" graus Ceusious')

except ValueError:
    print(f'''
    "{fahrenheit}" não é um numero.
    Somente numeros são aceitos, reais ou inteiros.
    Reinicie o programa e tente novamente.''')
