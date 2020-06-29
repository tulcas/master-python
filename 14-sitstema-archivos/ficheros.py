from io import open
import pathlib

# Abrir archivo
# archivo = open("/Users/andres/Documents/master-python/14-sitstema-archivos/fichero_texto.txt", "a+")

texto_con_ruta = str( pathlib.Path().absolute() )+ "/fichero_texto.txt"

print(texto_con_ruta)

archivo = open(texto_con_ruta, "a+")

# Escribir dentro del archivo
archivo.write("TEXTO DESDE PYTHON: >>>>>> The standard Lorem Ipsum passage, used since the 1500\n")

# Cerrar archivo // Siempre cerrar archivo al terminar la modificacion
archivo.close()