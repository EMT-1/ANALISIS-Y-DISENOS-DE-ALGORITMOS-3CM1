import time

def burbuja(arr):
    n = len(arr)
    start_time = time.time()  # Iniciar el temporizador
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end_time = time.time()  # Detener el temporizador
    elapsed_time = end_time - start_time  # Calcular el tiempo transcurrido
    return elapsed_time

def burbuja_optimizada(arr):
    n = len(arr)
    start_time = time.time()  # Iniciar el temporizador
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()  # Detener el temporizador
    elapsed_time = end_time - start_time  # Calcular el tiempo transcurrido
    return elapsed_time

def main():
    while True:
        print("Seleccione un método de ordenamiento:")
        print("1. Burbuja")
        print("2. Burbuja Optimizada")
        print("3. Salir")
        
        opcion = int(input("Ingrese su elección: "))
        
        if opcion == 1:
            n = int(input("Ingrese el tamaño de la lista: "))
            lista = [int(input(f"Ingrese el elemento {i + 1}: ")) for i in range(n)]
            tiempo = burbuja(lista)
            print("Lista ordenada usando Burbuja:", lista)
            print("Tiempo de ejecución: {:.10f} segundos".format(tiempo))
        elif opcion == 2:
            n = int(input("Ingrese el tamaño de la lista: "))
            lista = [int(input(f"Ingrese el elemento {i + 1}: ")) for i in range(n)]
            tiempo = burbuja_optimizada(lista)
            print("Lista ordenada usando Burbuja Optimizada:", lista)
            print("Tiempo de ejecución: {:.10f} segundos".format(tiempo))
        elif opcion == 3:
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
