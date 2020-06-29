print("############# EJEMPLO 3 ############# ")

def tabla(numero): #Se decllara la funcion
    print(f"Tabla de muiltiplicar del numero : {numero}" )# se ingresa numero por consola

    for contador in range(1, 11): # el contador comienza a recorrer el rango de a uno
        operacion = numero * contador # contador +1 en cada pasada
        # imprime el numero ingresado por el valor de contador en cada pasada y muestra el resultado de operacion

        print(f"{numero} x {contador} = {operacion} " ) 


    print("\n")


tabla_input = int(input("Ingrese el  numero de la tabla a calcular: ")) # Se ingresa por teclado numero
tabla(tabla_input) # Llamada a funcion tabla y se pasa variable ingresada por parametro.

tabla(8)
tabla(7)
tabla(10)

# Ejemplo 3.1
for i in range(1, 11):
    tabla(i)

