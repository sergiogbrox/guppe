"""
39- A importância de R$780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:

- O primeiro ganhador receberá 46%;
- O segundo receberá 32%;
- O terceiro receberá o restante;

Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

premio = 780_000.00
primeiro = premio*46/100
segundo = premio*32/100
terceiro = premio-primeiro-segundo

print(f'\nO premio de R${premio} dividido para os três ganhadores: '
      f'\nPrimeiro R${primeiro} '
      f'\nSegundo R${segundo} '
      f'\nTerceiro R${terceiro}')
