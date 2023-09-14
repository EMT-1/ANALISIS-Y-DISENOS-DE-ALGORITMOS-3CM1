import time

def busqueda_lineal(lista, elemento):
    inicio = time.time()
    encontrado = False
    for i in range(len(lista)):
        if lista[i] == elemento:
            encontrado = True
            break
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

        elemento_buscar = int(input("Ingresa el elemento a buscar: "))
        busqueda_lineal(lista, elemento_buscar)
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")
