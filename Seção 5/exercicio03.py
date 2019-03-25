"""
03- Leia um número real. Se o numero for positivo imprima a raiz quadrada. Do contrário,
imprima o número ao quadrado.
"""

numero = float(input('Digite um número real: \n'))

if numero >= 0:
    print(numero**0.5)
else:
    print(numero**2)
