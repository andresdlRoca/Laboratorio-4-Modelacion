'''
Para este ejercicio, la distribucion geometrica se utilizara
como la distribucion de probabilidad discreta. La distribucion geometrica
esta definida para valores enteros positivos y tiene un unico parameto, p,
que representa la probablidad de exito de un experimento de Bernoulli.
La funcion de probabilidad de la distribucion geometrica es:

P(x=k) = p * (1-p)^(k-1)


Donde X es la variable aleatoria geometrica y k es el valor que toma
la variable aleatoria.

Para este caso se utilizara p=0.2 como ejemplo.
'''

import numpy as np
import matplotlib.pyplot as plt

# Parametros
p = 0.2
n = 1000000

# Generacion de variables aleatorias utilzando la transformada inversa
def generate_geometric(p, size):
    u = np.random.rand(size)

    '''
    Este calculo implica tomar el logaritmo del valor aleatorio y aplicar una
    formula para obtener el valor de la variable aleatoria geometrica.
    '''
    x = np.floor(np.log(u) / np.log(1-p)) + 1
    return x.astype(int)

# Generacion de valores aleatorios
random_values = generate_geometric(p, n)

# Calculo de medias aritmeticas parciales
'''
Acumula los valores aleatorios generados y divide entre el numero de elementos acumulados
hasta ese punto
'''
partial_means = np.cumsum(random_values) / np.arange(1, n+1)

# Valor verdadero de la media
true_mean = 1 / p

# Grafico
plt.figure(figsize=(10, 6))
plt.plot(range(1, n + 1), partial_means, label='Medias Parciales')
plt.axhline(y=true_mean, color='r', linestyle='--', label='Media Verdadera')
plt.xlabel('n')
plt.ylabel('sn')
plt.legend()
plt.title('Convergencia de Medias Parciales a la Media Verdadera')
plt.show()

'''
En esta grafica la linea roja punteada representa la media verdadera de la distribucion
geometrica, mientras que la linea azul representa las medias aritmeticas parciales a medida
que n aumenta. Conforme n crece, la funcion n->sn oscila alrededor de la media verdadera
y se aproxima cada vez mas a ese valor a medida que aumenta el numero de muestras.

Se puede utilizar el valor de p para observar como cambia el comportamiento de las
medias parciales en relacion a la media verdadera. Por ejemplo, si p=0.5, la media
verdadera es 2, y la grafica de las medias parciales oscilara alrededor de ese valor
a medida que n crece.
'''

'''
El comportamiento observado en la grafica tiene que ver con el concepto de la ley del
los grandes numeros y como de realciona con la distribucion geometrica y las medias
aritmeticas parciales.

La ley de los grandes numeros establece que, si se tienen variables aleatorias
independientes e identicamente distribuidas, entonces la media aritmetica de esas
variables aleatorias se aproxima a la media verdadera de la distribucion a medida
que el numero de muestras aumenta. En este caso, las variables aleatorias son
independientes e identicamente distribuidas, ya que cada una de ellas sigue una
distribucion geometrica con el mismo parametro p. Por lo tanto, la ley de los numeros
grandes se cumple para este caso.

Por otro lado, la distribucion geometrica describe la cantidad de ensayos
independientes de un experimento de Bernoulli que se deben realizar hasta obtener
el primer exito. Por lo tanto, la media de la distribucion geometrica es 1/p, ya que
se espera que el primer exito ocurra en el ensayo 1/p. Por lo tanto, la media verdadera
de la distribucion geometrica es 1/p.

El comportamiento de la grafica refleja como las medias aritmeticas parciales
convergen hacia la media verdadera de la distribucion geometrica a medida que aumenta el
size de la muestra, en concordancia con la ley de los grandes numeros.
'''