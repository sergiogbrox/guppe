"""
4- Leia um  número real e imprima o resultado do quadrado desse número.
"""

print("\nDigite um valor inteiro para ser calculado sua raiz quadrada:\n ")

numero = input()

try:
    numero = int(numero)
    print(f'A raiz quadrada de "{numero}" é: {numero ** 0.5}')

except ValueError:
    print(f'''
    "{numero}" não é um numero inteiro.
    Somente numeros inteiros são aceitos.
    Reinicie o programa e tente novamente.''')
