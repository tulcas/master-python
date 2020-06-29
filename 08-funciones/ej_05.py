# Ejemplo 5: Parametros opcionales y return (o devolver datos a la funcion)
'''
def funcionCalculadora():

    print( "########## CALCULADORA BASICA ##########" )
        
    print("Para SUMA igresa 1")
    print("Para RESTA igresa 2 ")
    print("Para MULTIPLO igresa 3")
    print("Para DIVISION igresa 4")
    opcion = int(input("Ingrese una opcion:  ")):w

    print( "AHORA INGRESE LOS VALORES" )
    num1 = int(input("Ingresa un valor: "))
    num2 = int(input("Ingresa otro valor: "))

    if opcion == 1:
        
        return (print(f"La SUMA de ambos numeros es: {num1 + num2}") )
    elif opcion == 2:
        return (print(f"La RESTA de ambos numeros es: {num1 - num2}") )
    elif opcion == 3:
        return (print(f"El MULTIPLO de ambos numeros es: {num1 * num2}") )
    elif opcion == 4:
        return (print(f"La DIVISION de ambos numeros es: {num1 / num2}") )
    else:
        return (print("Fin de calculadora") )

funcionCalcGGuladora()
'''

# Ejemplo 5

def func_saludar(nombre):
    saludo = f"Hola, saludos estimado: {nombre} "
    
    return saludo


nombre = "Andresito"
print(func_saludar(nombre))


# Ejemplo 6
print( "########## Ejemplo 6 ##########" )

def func_Calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = " " 
    cadena += "Suma: " + str(suma)



# Ejemplo 7
print( "\n ########## Ejemplo 7 ##########" )

def func_GetNombre(nombre):
    texto = f"El nombre ingresado es: {nombre}"
    return texto

def func_GetApellido(apellido):
    texto = f"El apellido ingresado es: {apellido}"
    return texto

def func_NombreApellido(nombre, apellido):
    texto = func_GetNombre(nombre) + " -- " + func_GetApellido(apellido)
    return texto

print(func_GetNombre("Victor"), " -- ", func_GetApellido("Robles WEB") )

print( func_NombreApellido("Andres","Figuera") )

import os
os.system ("clear") 


# Ejemplo 8: Funciones Lambda

print( "\n ########## Ejemplo 8 ##########" )

dime_el_year = lambda year: f"El año es {year * 50 }"

print(dime_el_year(2034))