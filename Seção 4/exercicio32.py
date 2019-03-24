"""
32- Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
"""

print(f'\nDigite um valor inteiro para ser calculada '
      f'a soma do sucessor de seu triplo com o antecessor de de seu dobro.')

valor = input()

try:

    valor = int(valor)
    print(f'\nO sucessor do triplo de {valor} é {valor*3+1}, o antecessor de seu dobro é {valor*2-1}.'
          f'\nA soma de {valor*3+1} com {valor*2-1} é {(valor*3+1)+(valor*2-1)}.')

except ValueError:

    print(f'\nSomente numeros inteiros são aceitos, feche o programa e tente novamente.')
