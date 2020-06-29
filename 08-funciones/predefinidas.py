import os

nombre = "Victor Robles"


# Funciones Generales
print( type(nombre) )

# Detectar el tipado
comprobar = isinstance(nombre, str) # Comprueba si la variable es de tipo str
if comprobar:
    print("Esa variable es un string ")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un tipo de dato FLOAT")
else:
    print("La variable es de tipo FLOAT")

# Limpiar espacis String

frase = "       Mi contenido       "
print(frase)
print( frase.strip() )

# Eliminar Variables
year = 2022
print(year)
del year



# Comprobar variable vacia

texto = " ff "

if len(texto) <= 0:
    print("La variable esta vacia ")
else:
    caracteres = len(texto)
    print( f"La la varibale: {texto} tiene: {caracteres} caracteres " )


# Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida") )

# Reemplazar palabras en un string
nueva_frase = frase.replace("vida","moto")
print(nueva_frase)


# Mayusculas y minusculas

print(nombre)
print(nombre.lower() )
print(nombre.upper() )











