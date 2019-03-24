"""
42- Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-
se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
ele paga 7% de imposto sobre o salário-base.
"""

try:

    base = float(input("Digite o salário-base:"))
    
    print(f'\nO salário a receber é: R${base+(base*5/100)-(base*7/100)}')

except ValueError:

    print('Somente números são aceitos. Feche o programa e tente novamente')
