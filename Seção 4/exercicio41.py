"""
41- Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
"""

try:

    valor = float(input("Digite o valor da hora de trabalho: \nR$"))
    horas = float(input("Digite o numero de horas trabalhados: \n"))
    print(f'O valor a ser pago e: R${((valor*horas)*10/100)+valor*horas}')

except ValueError:

    print(f'Somente numeros são aceitos. Feche o programa e tente novamente,')
