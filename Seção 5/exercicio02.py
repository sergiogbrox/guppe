"""
02- Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
Se o número for negativo, mostre uma mensgem dizendo que o número é invalido.
"""

numero = int(input("Digite um número para ser calculada sua raiz quadrada:\n"))

if numero >= 0:
    print(numero**0.5)
else:
    print('Erro: Número invalido')
