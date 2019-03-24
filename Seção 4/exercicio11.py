"""
11- Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
(quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade
em km/h e M em m/s.
"""

print("Digite uma velocidade em m/s (metros por segundo) para ser convertida em km/h (quilômetros por hora).")

ms = input()

try:
    ms = float(ms)
    print(f'\n "{ms}m/s " é equivalente a: {ms * 3.6}km/h.')

except ValueError:
    print(f'''
    "{ms}" não é um numero.
    Somente numeros são aceitos, inteiros ou reais.
    Feche o programa e tente novamente.''')
