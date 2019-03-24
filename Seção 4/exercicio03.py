"""
3 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
"""

print("\nDigite tres valores inteiros para serem somados.")

valor1 = input("\nDigite o primeiro valor: ")
valor2 = input("\nDigite o segundo valor: ")
valor3 = input("\nDigite o terceiro valor: ")

try:
    valor1 = int(valor1)
    valor2 = int(valor2)
    valor3 = int(valor3)

    print(f'\nO resultado da soma é: {valor1 + valor2 + valor3}')

except ValueError:
    print(f'''
    Um ou mais destes valores não são numeros inteiros:
    "{valor1}, {valor2}, {valor3}"
    Somente numeros inteiros são aceitos.
    Reinicie o programa e tente novamente.''')
