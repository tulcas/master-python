"""
Ejercicio 05
Hacer un programa que muestre todos los numeros entre dos numeros
que ingrese el usuario.

"""

print(" ## Muestra listado de numeros entre dos valores: ##")

num1 = int(input("Ingresa un valor: "))
num2 = int(input("Ingresa otro valor: "))

if num1 < num2:
    for i in range(num1, num2+1 ):
        print(f"{i}")
else:
    print("El primer numero debe ser mayor al segundo...")