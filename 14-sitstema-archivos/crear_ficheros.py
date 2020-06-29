from io import open
import pathlib

# Abrir archivo
texto_con_ruta = str( pathlib.Path().absolute() ) + "/fichero_texto.txt"
archivo_lectura = open(texto_con_ruta, "r")

# Leer contenido
#contenido = archivo_lectura.read()
#print(contenido) 

# Leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

print(lista)

for i in lista:
    if i.isdecimal():
        print(i)
    print("- " + i.upper())