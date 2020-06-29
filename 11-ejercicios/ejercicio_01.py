"""
Ejercicio.1
Hacer un programa que tenga una lista de 8 numeros enteros

- Recorrer lista y mostrarla
- Ordenarla y mostrarla
- Crear una funcion que recorra listas de numeros y devuelva un string
- Mostrar su logitud
- Buscar algun elemento (que el usuario ingrese por teclado)

"""
# - Crear una funcion que re corra listas de numeros y devuelva un string
def mostrarLista(lista):
    resultado = ""

    for i in lista:
        resultado += "Elemento: " + str(i)
        resultado += "\n"
    return resultado


# Hacer un programa que tenga una lista de 8 numeros enteros
numeros = [13, 64, 52, 73, 21, 7, 91, 63]
print("******************** Funcion mostrarLista ********************")
print(mostrarLista(numeros))

#- Recorrer lista y mostrarla
print("******************** Recorrer lista y mostrarla ********************")
for i in numeros:
    print(i)


print("****************** Ordenar y Mostrar ********************")
#- Ordenarla y mostrarla
numeros.sort()
print(mostrarLista(numeros))
print("****************** Mostrar su logitud ********************")
#- Mostrar su logitud
print(f"La longitud de las lista es: ", len(numeros))


print("****************** Buscar algun elemento  ********************")

# Buscar algun elemento (que el usuario ingrese por teclado)

try:

    buscar  = int(input("Ingrese un numero para buscar en la lista: "))
    print(buscar in numeros)


    if buscar != False:
        print(f"El numero {buscar} se encuentra en la posicion", numeros.index(buscar))
except:
    print("El numero no esta en la lista...lo siento...")


