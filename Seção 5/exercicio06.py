num1 = int(input('1° número: '))
num2 = int(input('2° número: '))

if num1 > num2:
    print(f'{num1} é maior, sua diferença é de {num1-num2}')
elif num1 == num2:
    print('Os números são iguais')
else:
    print(f'{num2} é maior, sua diferença é de {num2 - num1}')
