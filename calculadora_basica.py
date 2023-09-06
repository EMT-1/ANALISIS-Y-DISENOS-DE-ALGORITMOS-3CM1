import math
import time
import os

# Función para medir el tiempo de ejecución
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        resultado = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tiempo de ejecución: {elapsed_time} segundos")
        return resultado
    return wrapper

# Funciones
def espacio(x):
    if x >= 1:
        print("")
        x = x - 1

wait = time.sleep
blank = os.system('cls')

# Bucle
while True:
    # Seleccion de operaciones
    print("""Selecciona la operacion deseada:
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division exacta
6. Potencia
7. Apagar calculadora""")
    espacio(1)

    # Switch_01
    c = int(input())

    # Apagar calculadora
    if c == 7:
        print("Gracias por usar esta calculadora")
        wait(2)
        quit()

    # Seleccion de numeros
    else:
        print("Escribe el primer numero")
        a = int(input())
        print("Escribe el segundo numero")
        b = int(input())
        espacio(2)
        print("El resultado de esta operacion és:")

        # Suma
        if c == 1:
            @medir_tiempo
            def suma(a, b):
                return a + b

            resultado = suma(a, b)
            print(resultado)
            print("")

        # Resta
        if c == 2:
            @medir_tiempo
            def resta(a, b):
                return a - b

            resultado = resta(a, b)
            print(resultado)
            print("")

        # Multiplicacion
        if c == 3:
            @medir_tiempo
            def multiplicacion(a, b):
                return a * b

            resultado = multiplicacion(a, b)
            print(resultado)
            print("")

        # Division
        if c == 4:
            @medir_tiempo
            def division(a, b):
                return a / b

            resultado = division(a, b)
            print(resultado)
            print("")

        # Division exacta
        if c == 5:
            @medir_tiempo
            def division_exacta(a, b):
                return a // b

            resultado = division_exacta(a, b)
            print(resultado)
            print("")
