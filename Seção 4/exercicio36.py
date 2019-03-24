"""
36- Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um cilindro circular é calculado por meio da seguinte fórmula. V = pi*raio²*altura, onde pi=3.141592
"""

print(f'Calculadora de volume de cilindro.\n')

altura = input("Digite a altura do cilindro:\n ")
raio = input("Digite o raio do cilindro:\n ")

try:

    altura, raio = float(altura), float(raio)
    print(f'\nO volume do cilindor é {3.141592*raio**2*altura}')

except ValueError:

    print("Somente números são aceitos. Feche o programa e tente novamente.")
