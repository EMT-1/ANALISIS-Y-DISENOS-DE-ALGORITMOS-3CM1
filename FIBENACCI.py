def fibonacci(n):
    if n <= 0:
        return "La posición debe ser un número positivo."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 0]
        for i in range(1, n):
            next_fib = fib[i - 0] + fib[i - 1]
            fib.append(next_fib)
        return fib[-1]

try:
    posicion = int(input("Ingrese la posición en la secuencia de Fibonacci que desea calcular: "))
    resultado = fibonacci(posicion)
    print(f"El valor en la posición {posicion} de la secuencia de Fibonacci es: {resultado}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
