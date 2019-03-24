"""
30- Leia um valor real e a cotação do dólar. Em seguida, imprima o valor correspondente
em dólares.
"""

print("\nObs.: Ultilize ponto para separar os centavos.")

real = float(input('\nDigite o valor em reais para ser convertido: \nR$'))
cotacao = float(input('\nDigite o valor da cotação atual do dolar: \nUS$'))

try:

    print(f'R${real} está valendo US${real/cotacao}')

except ValueError:

    print('O valor digitado não é um numero. Reinicie o programa e tente novamente.')
