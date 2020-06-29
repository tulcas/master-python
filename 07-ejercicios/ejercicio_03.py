'''
Ejercicio 3. 
Ecribir un programa que muestre los cuadrados (numero multiplicado por si mismo) de los 60 primeros numeros 
naturales.

- Resolver con for y while

'''

# While

contador = 0
while contador <= 10:
    cuadrado =  contador * contador
    print(f"El cuadradode de {contador} es {cuadrado}")

    contador += 1

# For

for i in range(10):
    cuadrado2 = i * i
    print(f"El cuadradode de {i} es {cuadrado2}")