"""
28- Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos
três valores lidos.
"""

print(f'\nDigite trẽs valores para que seja feita a soma dos quadrados dos trés  valores: \n')

valor1 = input('Digite o primeiro valor: \n')
valor2 = input('Digite o segundo valor: \n')
valor3 = input('Digite o terceiro valor: \n')

try:
    valor1 = float(valor1)
    valor2 = float(valor2)
    valor3 = float(valor3)
    print(f'A soma dos quadrados é: {valor1**2+valor2**2+valor3**2}')

except ValueError:

    print(f'''
    Um destes valores não é um numero:
    {valor1}, {valor2}, {valor3}
    
    Somente números são aceitos, reais ou inteiros.
    Feche o programa e tente novamente.''')
