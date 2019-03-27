lab = 2 * float(input('Digite a nota de laboratório: '))
ava = 3 * float(input('Digite a nota de laboratório: '))
exa = 5 * float(input('Digite a nota de laboratório: '))

media = (lab + ava + exa) / 10

if media>=5 and media<=10:
    print(f'Aprovado média {media}')
elif media<5 and media>=3:
    print(f'Recuperação média {media}')
elif media<3 and media>=0:
    print(f'Reprovado média {media}')
else:
    print('invalido')
