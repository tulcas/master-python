"""
FUNCIONES:
Una funcion es un conjunto de intrucciones agrupadas bajo un nombre
concreto que pueden reutilizarse invocando a la funcion tantas veces como sea necesario.

declaracion:

def nombreFuncion(parametros):
    #conjunto de intrucciones

invocar funcion:
nombreFuncion(mi_parametro)

Puedo invocarla las veces que quiera:
nombreFuncion(mi_parametro)
nombreFuncion(mi_parametro)
nombreFuncion(mi_parametro)



"""

# Ejemplo

print("############# EJEMPLO 1 ############# ")

# Definir Funcion
def muestraNombres():
    print("Victor")
    print("Andres")
    print("Ricardo")
    print("Jose")
    print("\n")

# Invocar funcion
# Ejemplo 1

print("")

for i in range (1, 5):
    muestraNombres()

# Ejemplo 2: Parametros

print("############# EJEMPLO 2 ############# ")



# Ejemplo 2 parametros

print("Ejemplo 2")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    
    if edad >= 18:
        print("Y eres mayor de edad...")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu Edad: "))
mostrarTuNombre(nombre, edad)

























