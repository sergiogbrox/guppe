"""
53- Faça um programa para ler as dimensões de um terreno (comprimento c e largura l),
bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno
com tela.
"""

c = float(input('Digite o comprimento do terreno em metros: '))
l = float(input('Digite a largura do terreno em metros: '))
valor = float(input('Digite o valor do metro da tela: '))

print(f'Será necessário {c*l} metros de tela. O total a ser cobrado é R${c*l*valor}')
