import time

def busqueda_binaria(lista, elemento):
    inicio = time.time()
    encontrado = False
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            encontrado = True
            break
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    fin = time.time()
    tiempo_ejecucion = fin - inicio

    if encontrado:
        print(f"El elemento {elemento} se encontró en la lista.")
    else:
        print(f"El elemento {elemento} no se encontró en la lista.")

    print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")

if __name__ == "__main__":
    try:
        n = int(input("Ingresa la longitud de la lista: "))
        lista = []
        for i in range(n):
            elemento = int(input(f"Ingresa el elemento {i + 1}: "))
            lista.append(elemento)

        lista.sort()  # Asegura que la lista esté ordenada para la búsqueda binaria.

        elemento_buscar = int(input("Ingresa el elemento a buscar: "))
        busqueda_binaria(lista, elemento_buscar)
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")
