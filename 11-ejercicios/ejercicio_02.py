"""
Ejercicio 2.
Escribir un programa que añada valores a una lista mientras
que el valor no supere los 120 caracteres.

Plus: usar while y for dos maneras.
"""

colecccion = []

for i in range (0, 10):
    colecccion.append(f" Añadir elemento numero: {i}") 
    print("Elemento añadido: " + colecccion[i])

print(colecccion)


