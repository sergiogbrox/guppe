"""
38- Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu
um aumento de 25%.
"""

print(f'\nDigite o valor de seu salário para ser calculado seu aumento de 25%:')

salario = input('R$')

try:

    salario = float(salario)
    print(f'\nSeu novo salário é de R${salario+(salario*25/100)}')

except ValueError:

    print('Somente numeros são aceitos. Feche o programa e tente novamente.')
