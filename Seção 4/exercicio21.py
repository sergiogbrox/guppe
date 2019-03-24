"""
21- Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula
de conversão é: K = L*0,45, sendo K a massa em quilogramas e L a massa em libras.
"""

print(f'\nDigite um valor de massa em libras para ser convertido em quilogramas: \n')

libras = input()

try:

    libras = float(libras)
    print(f'\n"{libras} libras" é equivalente a: {libras*0.45} quilogramas.')

except ValueError:

    print(f'''
    "{libras}" não é um número.
    Somente números são aceitos, inteiros ou reais.
    Feche o programa e tente novamente.''')
