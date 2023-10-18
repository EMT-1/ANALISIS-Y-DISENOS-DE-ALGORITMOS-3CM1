import random
import time
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

def measure_execution_time(sorting_algorithm, data):
    start_time = time.time()
    sorting_algorithm(data)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    num_arrays = 100
    array_sizes = [random.randint(1,100) for _ in range(num_arrays)]
    execution_times = []

    for size in array_sizes:
        data = generate_random_array(size)
        time_taken = measure_execution_time(quicksort, data)
        execution_times.append(time_taken)

    # Generar la gráfica
    plt.plot(array_sizes, execution_times, marker='o')
    plt.xlabel('Tamaño del arreglo')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempo de ejecución de Quicksort en 100 arreglos aleatorios')
    plt.grid(True)
    plt.show()
