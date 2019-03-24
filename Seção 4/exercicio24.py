"""
24- Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. A fórmula
de conversão é: M*0,000247, sendo M a área em metros quadrados e A
a área em acres.
"""

print(f'\nDigite um valor de área em metros quadrados para ser convertido para acres: \n')

metros = input()

try:

    metros = float(metros)
    print(f'\n"{metros} metros quadrados" é equivalente a: {metros*0.000247} acres.')

except ValueError:

    print(f'''
    "{metros}" não é um número.
    Somente números são aceitos, reais ou inteiros.
    Feche o programa e tente novamente.''')
