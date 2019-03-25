"""
nota1 = float(input('Digite nota 1: '))
nota2 = float(input('Digite nota 2: '))

if nota1 in range(0, 11) and nota2 in range(0, 11):
    print((nota1+nota2)/2)
else:
    print('Uma ou mais notas não são validas.')
"""

# Desta forma gasta menos processamento pois não precisa gerar ranges:

nota1 = float(input('Digite nota 1: '))
nota2 = float(input('Digite nota 2: '))

if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
        print((nota1 + nota2) / 2)
else:
    print("invalida")
