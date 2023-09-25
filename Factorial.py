def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número para calcular su factorial: "))

# Calcular y mostrar el factorial
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
