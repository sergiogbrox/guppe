"""
26- Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A fórmula de conversão é: H=m*0,0001, sendo M a área em metros quadrados e H a
área em hectares.
"""

print(f'\nDigite um valor em metros quadrados para ser convertido para hectares: \n')

metros = input()

try:

    metros = float(metros)
    print(f'\n"{metros} metros quadrados é equivalente a: {metros*0.0001} hectares.')

except ValueError:

    print(f'''
    "{metros}" não é um número.
    Somente números são aceitos, inteiros ou reais.
    Feche o programa e tente novamente.''')
