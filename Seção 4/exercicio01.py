"""
1. Faça um programa que leia um número inteiro e o imprima.
"""

numero = input("Digite um numero inteiro: ")

try:
    numero = int(numero)
    print(f'Parabéns, o numero {numero} é um numero inteiro!')

except ValueError:
    print("Somente numeros inteiros são aceitos. Reinicie o programa e tente novamente.")
