import time
import matplotlib.pyplot as plt

def es_seguro(tablero, fila, columna, n):
    for i in range(columna):
        if tablero[i] == fila or tablero[i] - i == fila - columna or tablero[i] + i == fila + columna:
            return False
    return True

def resolver_n_reinas_backtracking_util(tablero, columna, n, soluciones):
    if columna == n:
        soluciones.append(tablero[:])
        return
    
    for fila in range(n):
        if es_seguro(tablero, fila, columna, n):
            tablero[columna] = fila
            resolver_n_reinas_backtracking_util(tablero, columna + 1, n, soluciones)

def resolver_n_reinas_backtracking(n):
    tablero = [-1] * n
    soluciones = []
    resolver_n_reinas_backtracking_util(tablero, 0, n, soluciones)
    return soluciones

def resolver_n_reinas_alpha_beta_util(tablero, columna, n, alpha, beta, soluciones):
    if columna == n:
        soluciones.append(tablero[:])
        return
    
    for fila in range(n):
        if es_seguro(tablero, fila, columna, n):
            tablero[columna] = fila
            resolver_n_reinas_alpha_beta_util(tablero, columna + 1, n, alpha, beta, soluciones)
            alpha = max(alpha, fila + 1)
            if alpha >= beta:
                return

def resolver_n_reinas_alpha_beta(n):
    tablero = [-1] * n
    soluciones = []
    resolver_n_reinas_alpha_beta_util(tablero, 0, n, float('-inf'), float('inf'), soluciones)
    return soluciones

def resolver_n_reinas_heuristica_util(tablero, columna, n, soluciones):
    if columna == n:
        soluciones.append(tablero[:])
        return
    
    for fila in range(n):
        if es_seguro(tablero, fila, columna, n):
            tablero[columna] = fila
            resolver_n_reinas_heuristica_util(tablero, columna + 1, n, soluciones)
            if soluciones:
                return

def resolver_n_reinas_heuristica(n):
    tablero = [-1] * n
    soluciones = []
    resolver_n_reinas_heuristica_util(tablero, 0, n, soluciones)
    return soluciones

def ejecutar_experimento(algoritmo, valores_n):
    tiempos = []
    lista_soluciones = []
    for n in valores_n:
        tiempo_inicio = time.time()
        soluciones = algoritmo(n)
        tiempo_fin = time.time()
        tiempos.append(tiempo_fin - tiempo_inicio)
        lista_soluciones.append(soluciones)
        print(f"Tiempo para N={n}: {tiempos[-1]} segundos")
        print(f"Soluciones para N={n}:\n{lista_soluciones[-1]}\n")
    return tiempos, lista_soluciones

def principal():
    try:
        # Tamaños del problema (N)
        valores_n = [4, 8, 12]

        # Medir el tiempo para la implementación inicial
        tiempos_backtracking, _ = ejecutar_experimento(resolver_n_reinas_backtracking, valores_n)

        # Medir el tiempo para la implementación con poda alfa-beta
        tiempos_alpha_beta, _ = ejecutar_experimento(resolver_n_reinas_alpha_beta, valores_n)

        # Medir el tiempo para la implementación con heurística inteligente
        tiempos_heuristica, _ = ejecutar_experimento(resolver_n_reinas_heuristica, valores_n)

        # Graficar los tiempos
        plt.plot(valores_n, tiempos_backtracking, label='Backtracking')
        plt.plot(valores_n, tiempos_alpha_beta, label='Poda Alfa-Beta')
        plt.plot(valores_n, tiempos_heuristica, label='Heurística')
        plt.xlabel('N')
        plt.ylabel('Tiempo (segundos)')
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    principal()
