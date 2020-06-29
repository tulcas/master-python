"""
# Ejercicio 04
Pedir dos numeros a el usr y crear las funciones basicas de una calculadora y mostrar por  
pantalla..
"""

print( "########## CALCULADORA BASICA ##########" )
    
print("Para SUMA igresa 1")
print("Para RESTA igresa 2 ")
print("Para MULTIPLO igresa 3")
print("Para DIVISION igresa 4")
opcion = int(input("Ingrese una opcion:  "))

print( "AHORA INGRESE LOS VALORES" )
num1 = int(input("Ingresa un valor: "))
num2 = int(input("Ingresa otro valor: "))

if opcion == 1:
    print(f"La SUMA de ambos numeros es: {num1 + num2}")
elif opcion == 2:
    print(f"La RESTA de ambos numeros es: {num1 - num2}")
elif opcion == 3:
    print(f"El MULTIPLO de ambos numeros es: {num1 * num2}")
elif opcion == 4:
    print(f"La DIVISION de ambos numeros es: {num1 / num2}")
else:
    print("Fin de calculadora")

