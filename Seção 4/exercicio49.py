"""
49- Faça um programa que leia o horário (hora, minuto e segundo) de início e a duração, em segundos, de uma experiencia
biológica. O programa deve resultar com o novo horário (hora, minuto e segundo) do termino da mesma.
"""
print("Digite o horario inicial:")
hora_ini = int(input("Hora: "))
min_ini = int(input("Minuto: "))
seg_ini = int(input("Segundo: "))

tempo_inicial = int((hora_ini*3600)+(min_ini*60)+seg_ini)
tempo_percorrido = int(input('Digite os segundos percorridos: '))

total = int(tempo_inicial+tempo_percorrido)

print(f'O tempo final foi: {int(total / 3600 % 60)}:{int(total / 60 % 60)}:{int(total % 60)}')
