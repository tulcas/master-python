"""
Ejercicio.08

Cuanto es el x% de un numero
por ejemplo: 20% de  150

"""

print( "INGRESE UN VALOR y EL PORCENTAJE % DESADO" )
num1 = int(input("Ingrese un valor: "))
porcentaje = int(input(f"Ingrese el porcentaje a calcular para {num1}: "))

print(f"El porcentaje es: {num1 * porcentaje / 100 } ")

