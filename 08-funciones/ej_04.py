print("############# EJEMPLO 4 ############# ")

# Parametros Opcionales.

def getEmpleado(nombre, dni = None):
    print("Empleado.")
    print(f"Nombre: {nombre} ")
    

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Andres Figuera", )