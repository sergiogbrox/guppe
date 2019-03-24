"""
Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
km/h e M em m/s.
"""

print("\n Digite uma velocidade em km/h (quilômetros por hora) para ser convertida em m/s (metros por segundo).\n")

kmh = input()

try:
    kmh = float(kmh)
    print(f'\n "{kmh}" km/h é equivalente a:{kmh / 3.6}')

except ValueError:
    print(f'''
    "{kmh}" não é um número.
    Somente numeros são aceitos, inteiros ou reais.
    Feche o programa e tente novamente.''')
