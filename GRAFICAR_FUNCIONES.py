import matplotlib.pyplot as plt
import numpy as np

# Rango de valores para el tamaño de entrada (n)
n = np.arange(1, 21)

# Funciones de las notaciones Big O
O_1 = np.ones_like(n)
O_log_n = np.log(n)
O_n = n
O_n_squared = n**2
O_2_power_n = 2**n
O_n_factorial = [np.math.factorial(i) for i in n]

# Crear gráfica
plt.figure(figsize=(12, 8))

plt.plot(n, O_1, label='O(1)')
plt.plot(n, O_log_n, label='O(log n)')
plt.plot(n, O_n, label='O(n)')
plt.plot(n, O_n_squared, label='O(n^2)')
plt.plot(n, O_2_power_n, label='O(2^n)')
plt.plot(n, O_n_factorial, label='O(n!)')

# Configuración de la gráfica
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Notaciones Big O')
plt.grid(True)
plt.legend()

# Mostrar gráfica
plt.ylim(0,100)
plt.show()
