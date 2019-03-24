"""
48- Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""

valor = int(input("Digite um valor em segundos para ser convertido em horas, minutos e segundos: "))
segundos = int(valor % 60)
minutos = int(valor/60 % 60)
horas = int(valor/60/60 % 60)
print(f'{horas}:{minutos}:{segundos}')
