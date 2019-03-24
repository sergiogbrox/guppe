"""
44- Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir pra atingir
seu objetivo.
"""

try:

    degrau = float(input('Digite a altura do degrau da escada: '))
    objetivo = float(input('Digite a altura que deseja subir: '))

    print(f'Para subir {objetivo} de altura voce deve subir {objetivo/degrau}')

except ValueError:

    print('Somente numeros são aceitos. Feche o programa e tente novamente.')
