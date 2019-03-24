"""
31- Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
"""

numero = input(f'\nDigite um numero inteiro para ser apresentado seu antecessor e seu sucessor:\n')

try:

    numero = int(numero)
    print(f'\n O antecessor de {numero} é {numero - 1} e o sucessor é {numero + 1}')

except ValueError:

    print('\n Somente numeros inteiros são aceitos. Feche o programa e tente novamente.')
