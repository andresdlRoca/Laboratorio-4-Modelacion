'''
*** Metodo de Transformada Inversa ***

El metodo de la transformada inversa es aplicable cuando se tiene una 
funcion de distribucion acumulativa (FDA) F(x) que es invertible.

1. Generar un numero aleatorio u en el intervalo [0,1) siguiendo una 
distribucion uniforme.

2. Encontrar x = F^-1(u) usando la FDA inversa F^-1(x).

La variable x generada de esta manera seguira la distribucion de 
probabilidad original F(x).


*** Metodo de Aceptacion y Rechazo ***

Este metodo es util cuando la funcion de densidad de probabilidad f(x) es 
conocida, pero es complicada de invertir para aplicar el metodo de 
transformada inversa.

1. Seleccionar una funcion de densidad de probabilidad g(x) que sea facil 
de muestrear y que pueda ser una "envolvente" para f(x).

2. Generar un numero aleatorio x a partir de g(x).

3. Generar otro numero aleatorio u en el intervalo [0,1) con una 
distribucion uniforme.

4. Calcular f(x)/(M * g(x)), donde M es una constante que hace que 
M * g(x) sea siempre mayor o igual a f(x).

5. Si u <= f(x)/(M * g(x)), aceptar x como una muestra de f(x); de 
lo contrario volver al paso 2.



*** Problema ***
1,000,000 estudiantes
400,000 mujeres
300,000 usan lentes
150,000 hombres usan lentes

1. P(estudiante sea mujer y use lentes)
2. P(estudiante sin lentes sea hombre)

Usar el metodo de Transformada Inversa porque las probabilidades estan
bien definidas y son faciles de calcular. Solo necesitamos generar 
un numero aleatorio y compararlo con la probabilidad de interes.

El Metodo de Aceptacion y Rechazo es mas adecuado para situaciones 
en las que la funcion de densidad de probabilidad es complicada 
y/o no se puede invertir facilmente. En este problema, ya tenemos todas 
las probabilidades que necesitamos, por lo que no hay necesidad de 
complicar el proceso con un metodo mas flexible pero mas complejo.


*** Analisis estadistico ***
Si 300,000 personas usan lentes y 150,000 hombres usan lentes, entonces
300,000 - 150,000 = 150,000 mujeres deben usar lentes.

El numero total de hombres es 1,000,000 - 400,000 = 600,000.

El numero de hombres que no usan lentes es 600,000 - 150,000 = 450,000.

El numero total de personas que no usan lentes es 
1,000,000 - 300,000 = 700,000.

'''
import random

# Numero de simulaciones
n_simulations = 1000000

# Primer escenario: Probabilidad de que sea una mujer y use lentes
prob_mujer_lentes = 150000 / 1000000
count_mujer_lentes = 0

# Segundo escenario: Probabilidad de que sea un hombre y no use lentes
# Nota: Se selecciona a alguien que no usa lentes (700,000 personas en total)
prob_hombre_sin_lentes = 450000 / 700000
count_hombre_sin_lentes = 0

# Simulacion
for _ in range(n_simulations):
    # Primer escenario
    u1 = random.random()
    if u1 < prob_mujer_lentes:
        count_mujer_lentes += 1

    # Segundo escenario
    u2 = random.random()
    if u2 < prob_hombre_sin_lentes:
        count_hombre_sin_lentes += 1

# Estimacion de las probabilidades mediante frecuencias relativas
estimated_prob_mujer_lentes = count_mujer_lentes / n_simulations
estimated_prob_hombre_sin_lentes = count_hombre_sin_lentes / n_simulations

print(
    f"Probabilidad estimada de que sea una mujer y use lentes: {estimated_prob_mujer_lentes}")
print(
    f"Probabilidad estimada de que sea un hombre y no use lentes: {estimated_prob_hombre_sin_lentes}")
