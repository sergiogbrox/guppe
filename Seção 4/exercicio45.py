"""
45- Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela
 ASCII para resolver o problema.
"""

# FORMA FEITA POR SERGIO COMPLETA:


try:

    letra = ord(input('\nDigite uma letra minúscula para ser convertida para maiuscula: '))

    if letra in range(97, 123):
        print(f'\nConversão: {chr(letra-32)}')

    else:
        print(f'\nERRO: "{chr(letra)}" não é uma letra minuscula. Feche o programa e tente novamente.')

except TypeError:

    print('\nERRO: Somente uma letra minúscula é aceita. Feche o programa e tente novamente.')


# FORMA FEITA POR SERGIO SIMPLIFICADA CONFORME ENSINAMENTOS DO CURSO (SEM USAR TABELA ASCII):

"""
letra = str(input("Digite a letra"))

print(f'{letra.lower()}')
"""

# FORMA FEITA POR PROFESSOR POREM ACEITA SÍMBOLOS E NÚMEROS:
"""
minusculo = input('Informe um caractere minúsculo: ')
print(f'O caractere {minusculo} em maiúsculo é {chr(ord(minusculo) - 32)}')
"""