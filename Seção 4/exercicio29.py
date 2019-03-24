"""
29- Leia quatro notas, calcule a média aritimética e imprima o resultado.
"""

print(f'\nDigite 4 notas para ser calculada a média aritimética:\n')

try:

    nota1 = float(input("Digite a primeira nota:\n"))
    nota2 = float(input("Digite a segunda nota:\n"))
    nota3 = float(input("Digite a terceira nota:\n"))
    nota4 = float(input("Digite a quarta nota:\n"))

    print(f'A média aritimetica é: {(nota1 + nota2 + nota3 + nota4)/4}')

except ValueError:

    print(f'''
    O valor digitado não é um número:
    Somente números são aceitos, reais ou inteiros.
    Feche o programa e tente novamente.''')
