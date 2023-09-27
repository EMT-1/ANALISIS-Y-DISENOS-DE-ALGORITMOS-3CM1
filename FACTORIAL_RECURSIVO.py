def factorial(numero):
	"""
	Calcula el factorial de un número de forma recursiva.
	"""
	if numero == 1:
		return 1
	else:
		return numero * factorial(numero - 1)
		
print(factorial(5))