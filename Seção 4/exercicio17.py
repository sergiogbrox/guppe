"""
17- Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C/2,54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
"""

print(f'\nDigite um valor em centímetros para ser convertido em polegadas:\n')

centimetros = input()

try:

    centimetros = float(centimetros)
    print(f'\n"{centimetros} centímetros" é equivalente a: {centimetros/2.54} polegadas')

except ValueError:

    print(f'''
    "{centimetros}" não é um número.
    Somente números são aceitos, reais ou inteiros.
    Feche o programa e tente novamente.''')
