"""
16- Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
A fórmula de conversão é: C=P*2,54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
"""

print(f"\nDigite um valor de comprimento em polegadas para ser convertido em polegadas:\n")

polegadas = input()

try:

    polegadas = float(polegadas)
    print(f'\n"{polegadas}" polegadas é equivalente a: {polegadas*2.54} centimetros.')

except ValueError:

    print(f'''
    "{polegadas}" não é um numero.
    Somente numeros são aceitos, reais ou inteiros.
    Feche o programa e tente novamente.''')
