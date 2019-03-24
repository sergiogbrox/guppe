"""
5- Leia um número real e imprima a quinta parte deste numero.
"""

print("\nDigite um numero inteiro para ser calculada sua quinta parte:\n ")

numero = input()

try:
    numero = int(numero)
    print(f'\nA quinta parte de "{numero}" é: {numero / 5}')

except ValueError:
    print(f'''
    "{numero}" não é um numero inteiro.
    Somente numeros inteiros são aceitos.
    Reinicie o programa e tente novamente''')
