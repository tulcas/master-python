# capturar excepciona y manejar errores en codigo 
# susceptible a fallos/errores
"""

try:
    nombre = input("Cual es tu nombre ?: ")
    if len(nombre) > 1:
            nombre_usuario = "El nombre es: " + nombre
            
    print(nombre_usuario)
except:
    print("Ha ocurrido un error, ingresa el nombre correctamente...")
else:
    print("Todo ha funcionado correctamente ")
finally:
    print("Find e la iteracion !!! ")


print("****************** Buscar algun elemento  ********************")
# Buscar algun elemento (que el usuario ingrese por teclado)
buscar  = int(input("Ingrese un numero para buscar en la lista: "))
print(buscar in numeros)

if buscar != False:
    print(f"El numero {buscar} se encuentra en la posicion", numeros.index(buscar))
"""
'''
# Multiples exepciones
try:
    numero = int( input("Ingresa un numero para elevarlo al cuadrado: ") )
    print("El cuadrado es: " + str (numero * numero) )
except TypeError:
    print("Debes convertir tus cadenas a enteros...")
#except ValueError:
    #print("Debes ingresar un entero...")
except Exception as error:
    print(type(error))
    print("Ha ocurrido un error: ", type(error).__name__)

    '''

# Excepciones personalizadas o Lanzar excepcion

try: 
    nombre = input("Introduce el nombre: ")
    edad = int( input("Introduce la edad: ") )

    if edad < 5 or edad > 110: 
        raise ValueError("La edad ingresada no es real...")
    elif len(nombre) <= 1 :
        raise ValueError("El nombre no es valido...")
    else:
        print(f"Bienvenido al Master en Python {nombre}" )
except ValueError:
    print(f"Ingresa datos validos!!! valor {edad} INVALIDO!")
