"""
33- Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.
"""

print(f'\nDigite a medida da lateral de um quadrado em cm para ser calculada sua área:')

lateral = input()

try:

    lateral = float(lateral)
    print(f'\nA área do quadrado é {lateral**2}cm².')

except ValueError:

    print(f'\nSomente numeros são aceitos. Feche o programa e tente novamente.')
