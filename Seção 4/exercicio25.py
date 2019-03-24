"""
25- Leia um valor de área em acres e apresente-o convertido em metros quadrados m². A
fórmula de conersão é: M=A*4048,58, sendo M a área em metros quadrados e A a
área em acres.
"""

print(f'\nDigite um valor de área em acres para ser convertido para metros quadrados: \n')

acres = input()

try:

    acres = float(acres)
    print(f'\n"{acres} acres" é equivalente a: {acres*4048.58} metros quadrados.')

except ValueError:

    print(f'''
    "{acres}" não é um número.
    Somente números são aceitos, inteiros ou reais.
    Feche o programa e tente novamente.''')
