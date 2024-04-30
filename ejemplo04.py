sueldo = input("Ingrese el sueldo de la persona: ")

sueldo = int(sueldo)

if sueldo <= 100:
	print('correcto')
else:
	if (sueldo >= 101) and (sueldo <= 110):
		print("Sobresaliente")
	else:
		print("Incorrecto")

