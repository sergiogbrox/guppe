sal = float(input("Salário: "))
emp = float(input("Empréstimo: "))

if emp > sal*20/100:
	print('Empréstimo não concedido.')
else:
	print('Empréstimo concedido.')
