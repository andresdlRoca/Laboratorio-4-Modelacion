import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución exponencial
lmbda = 0.5  # Parámetro de la distribución
n = 1000000  # Número de valores aleatorios a generar

# Generación de variables aleatorias utilizando el método de la transformada inversa
def generate_exponential(lmbda, size):
    u = np.random.rand(size)  # Genera 'size' números aleatorios entre 0 y 1
    x = -np.log(1 - u) / lmbda  # Transformada inversa
    return x

# Generación de valores aleatorios
random_values = generate_exponential(lmbda, n)

# Cálculo de medias aritméticas parciales
partial_means = np.cumsum(random_values) / np.arange(1, n + 1)

# Valor verdadero de la media
true_mean = 1 / lmbda

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(range(1, n + 1), partial_means, label='Medias Parciales')
plt.axhline(y=true_mean, color='r', linestyle='--', label='Media Verdadera')
plt.xlabel('n')
plt.ylabel('sn')
plt.legend()
plt.title('Convergencia de Medias Parciales a la Media Verdadera (Distribución Exponencial)')
plt.show()
