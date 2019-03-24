"""
37- Faça um prograa que leia o valor de um prouto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%
"""

print(f'Digite o valor de um produto para ser calculado o desconto de 12%')

valor = input('R$')

try:

    valor = float(valor)
    print(f'O valor do produto com desconto de 12% é R${valor-(valor*12/100)}')

except ValueError:

    print('Somente números são aceitos. Feche o programa e tente novamente.')
