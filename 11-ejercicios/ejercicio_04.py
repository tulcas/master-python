"""
Ejercicio 4
Crear un script que tenga 4 variables, una lista un string, un entero
y un booleano y que imprima un mensaje 
segun el tipo de dato de cada variable.

"""


# ***************************************
def comprobarType(var):
    tipo = None
    if type(var) == list:
        tipo = "LISTA"
    elif type(var) == str:
        tipo = "CADENA DE TEXTO"
    elif type(var) == int:
        tipo = "NUMERO ENTERO"
    elif type(var) == bool:
        tipo = "BOOLEANO"
    var = print(f"EL contenido de la variable es: {var} es del tipo: " + tipo  )
    return var
# ***************************************
mi_lista = ["Hola Mundo", 77]
titulo = "Master en Pyhton"
numero = 100
variablebool = True
# ***************************************
todo = [ mi_lista, titulo, numero, variablebool]
# ***************************************
for i in todo:
    print(comprobarType(i))
