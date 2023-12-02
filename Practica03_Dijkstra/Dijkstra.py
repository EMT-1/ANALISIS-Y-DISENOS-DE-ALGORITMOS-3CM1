import heapq
import time

class Grafo:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def add_edge(self, desde_vertice, hacia_vertice, peso):
        if desde_vertice in self.vertices and hacia_vertice in self.vertices:
            self.vertices[desde_vertice].append((hacia_vertice, peso))
            self.vertices[hacia_vertice].append((desde_vertice, peso))  # En caso de grafo no dirigido

    def dijkstra(self, inicio):
        distancias = {vertice: float('inf') for vertice in self.vertices}
        distancias[inicio] = 0
        pq = [(0, inicio)]

        while pq:
            distancia_actual, vertice_actual = heapq.heappop(pq)

            if distancia_actual > distancias[vertice_actual]:
                continue

            for vecino, peso in self.vertices[vertice_actual]:
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(pq, (distancia, vecino))

        return distancias

# Ejemplo de uso 1
grafo1 = Grafo()
grafo1.add_vertex("A")
grafo1.add_vertex("B")
grafo1.add_vertex("C")
grafo1.add_edge("A", "B", 3)
grafo1.add_edge("A", "C", 5)
grafo1.add_edge("B", "C", 2)

nodo_inicio = "A"

start_time = time.time()
result = grafo1.dijkstra(nodo_inicio)
end_time = time.time()

resultados = grafo1.dijkstra(nodo_inicio)
print("Distancias más cortas desde el nodo", nodo_inicio, "a los demás nodos en el caso 1:")
for nodo, distancia in resultados.items():
    print(f"Nodo: {nodo}, Distancia: {distancia}")

tiempo_ejecucion = end_time - start_time
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")

# Ejemplo de uso 2
grafo2 = Grafo()
grafo2.add_vertex("A")
grafo2.add_vertex("B")
grafo2.add_vertex("C")
grafo2.add_vertex("D")
grafo2.add_edge("A", "B", 2)
grafo2.add_edge("A", "C", 5)
grafo2.add_edge("C", "B", 7)
grafo2.add_edge("B", "D", 4)

nodo_inicio = "A"

start_time = time.time()
result = grafo2.dijkstra(nodo_inicio)
end_time = time.time()

resultados = grafo2.dijkstra(nodo_inicio)
print("Distancias más cortas desde el nodo", nodo_inicio, "a los demás nodos en el caso 2:")
for nodo, distancia in resultados.items():
    print(f"Nodo: {nodo}, Distancia: {distancia}")

tiempo_ejecucion = end_time - start_time
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")

# Ejemplo de uso 3
grafo3 = Grafo()
grafo3.add_vertex("A")
grafo3.add_vertex("B")
grafo3.add_vertex("C")
grafo3.add_vertex("D")
grafo3.add_vertex("E")
grafo3.add_edge("A", "B", 8)
grafo3.add_edge("A", "C", 9)
grafo3.add_edge("B", "D", 10)
grafo3.add_edge("C", "E", 2)
grafo3.add_edge("D", "C", 5)
grafo3.add_edge("E", "B", 13)


nodo_inicio = "A"

start_time = time.time()
result = grafo3.dijkstra(nodo_inicio)
end_time = time.time()

resultados = grafo3.dijkstra(nodo_inicio)
print("Distancias más cortas desde el nodo", nodo_inicio, "a los demás nodos en el caso 3:")
for nodo, distancia in resultados.items():
    print(f"Nodo: {nodo}, Distancia: {distancia}")

tiempo_ejecucion = end_time - start_time
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")

# Ejemplo de uso 4
grafo4 = Grafo()
grafo4.add_vertex("A")
grafo4.add_vertex("B")
grafo4.add_vertex("C")
grafo4.add_vertex("D")
grafo4.add_vertex("E")
grafo4.add_edge("A", "D", 4)
grafo4.add_edge("D", "C", 5)
grafo4.add_edge("C", "B", 8)
grafo4.add_edge("B", "E", 9)
grafo4.add_edge("E", "A", 15)

nodo_inicio = "A"

start_time = time.time()
result = grafo4.dijkstra(nodo_inicio)
end_time = time.time()

resultados = grafo4.dijkstra(nodo_inicio)
print("Distancias más cortas desde el nodo", nodo_inicio, "a los demás nodos en el caso 4:")
for nodo, distancia in resultados.items():
    print(f"Nodo: {nodo}, Distancia: {distancia}")

tiempo_ejecucion = end_time - start_time
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")

# Ejemplo de uso 5
grafo5 = Grafo()
grafo5.add_vertex("A")
grafo5.add_vertex("B")
grafo5.add_vertex("C")
grafo5.add_vertex("D")
grafo5.add_vertex("E")
grafo5.add_vertex("F")
grafo5.add_edge("A", "B", 5)
grafo5.add_edge("A", "C", 7)
grafo5.add_edge("B", "C", 9)
grafo5.add_edge("C", "D", 12)
grafo5.add_edge("C", "E", 15)
grafo5.add_edge("D", "F", 8)
grafo5.add_edge("E", "F", 11)

nodo_inicio = "A"

start_time = time.time()
result = grafo5.dijkstra(nodo_inicio)
end_time = time.time()

resultados = grafo5.dijkstra(nodo_inicio)
print("Distancias más cortas desde el nodo", nodo_inicio, "a los demás nodos en el caso 5:")
for nodo, distancia in resultados.items():
    print(f"Nodo: {nodo}, Distancia: {distancia}")

tiempo_ejecucion = end_time - start_time
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")