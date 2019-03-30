nota = -1

while nota < 0 or nota > 10:

    try:
        nota = int(input('Digite uma nota de 0 a 10:\n'))
        if nota < 0 or nota > 10:
            print('Erro: Numero invalido.\n')

    except ValueError:
        print('Erro: Numero invalido.\n')
        continue
else:
    print(f'A nota é: {nota}')
