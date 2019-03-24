"""
1. Faça um programa que leia um número real e o imprima.
"""

numero = input("\nDigite um numero real: ")

try:
    numero = float(numero)
    print(f'Parabéns, o numero "{numero}" é um numero real!')

except ValueError:
    print(f'''
    ATENÇÃO: "{numero}" não é um numero real.
    Somente numeros reais são aceitos. Exemplo: "2.36".
    Reinicie o programa e tente novamente.''')
