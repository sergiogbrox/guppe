"""
34- Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
A área do circulo é pi*raio²,considere pi=3.14152
"""

print(f'\nDigite o valor de raio de um circulo para ser calculada a área do circulo:')

raio = input()

try:

    raio = float(raio)
    print(f'\nA área do círculo é {3.14152*raio**2}.')

except ValueError:

    print(f'\nSomente números são aceitos. Feche o programa e tente novamente.')
