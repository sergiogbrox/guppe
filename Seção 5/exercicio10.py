alt = float(input("altura:"))
sex = input("sexo (m ou f):")


if sex is "m":
	print((72.7*alt)-58)
elif sex is "f":
	print((62.1*alt)-44.7)
else:
	print('inválido.')
