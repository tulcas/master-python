"""
Ejercicio 02

Escribir un Script que muestre por pantalla todos los numeros pares del 0 a 120

"""
contador = 1
resto = 0

for contador in range(1, 25):   
    if contador % 2 == 0:
        print(f"El numero: {contador} es un numero par")
