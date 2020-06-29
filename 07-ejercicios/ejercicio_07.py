"""
Ejercicio 07
Hacer un programa que muestre todos los numeros impares entre
dos numeros que decida el usuario.
"""

print( "INGRESE DOS VALORES PARA MOSTRAR TODOS LOS NUMEROS IMPARES ENTRE ELLOS" )
num1 = int(input("Ingresa un valor: "))
num2 = int(input("Ingresa otro valor: "))
if num1 < num2:
    for i in range(num1, num2 + 1): # i recorre el rango tomando el valor diferente en cada pasada
        if i%2 == 0: # En cada pasada i se divide por dos y verifica si es igual a 0
            print(f"{i} -> es PAR ") # Si el resultado es 0 lo imprime
        else:   
            print(f"{i} -> es IMPAR ") # Si el resultado es diferente de 0 lo imprime
else:
    print("El primer numnero debe ser MAYOR a el segundo...find el programa")









    