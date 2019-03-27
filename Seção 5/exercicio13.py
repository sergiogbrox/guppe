prova1 = float(input("Digite a nota de 0 a 100 da prova 1:"))
prova2 = float(input("Digite a nota de 0 a 100 da prova 2:"))
prova3 = 2 * float(input("Digite a nota de 0 a 100 da prova 3:"))

media = (prova1 + prova2 + prova3) / 4

if media>60 and media<100:
    print(f'Média:{media}\nAprovado!')
elif media<60 and media>0:
    print(f'Média:{media}\nReprovado!')
else:
    print('invalido')
