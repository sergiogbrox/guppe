"""
52- Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente
ao valor que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do
prêmio com base no valor investido.
"""

ap1 = float(input('Digite o valor apostado pelo apostador 1:'))
ap2 = float(input('Digite o valor apostado pelo apostador 2:'))
ap3 = float(input('Digite o valor apostado pelo apostador 3:'))

prem = float(input('Digite o valor do prêmio: '))

print(f'''
Apostador 1 receberá: {(prem/100*(ap1+ap2+ap3)*ap1/100)}
Apostador 2 receberá: {(prem/100*(ap1+ap2+ap3)*ap2/100)}
Apostador 3 receberá: {(prem/100*(ap1+ap2+ap3)*ap3/100)}
''')
