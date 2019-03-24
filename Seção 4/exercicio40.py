"""
40- Uma empresa contrata um encanador a R$30,00 por dia. Faça m programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda.
"""

dias = input("Digite quantos dias vai precisar do encanador:")
valor = 30
desconto = float(dias)*float(valor)*8/100

try:
    dias = float(dias)
    print(f'O valor a ser pago ao encanador é de R${dias*valor+desconto}')

except ValueError:

    print('Somente números são aceitos, feche o programa e tente novamente.')
