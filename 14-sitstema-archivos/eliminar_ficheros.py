# Eliminar
from io import open
import pathlib
import shutil
import os


# Eliminar
'''
ruta_origen = str( pathlib.Path().absolute() ) + "/fichero_texto_movido.txt"
ruta_origen = str( pathlib.Path().absolute() ) + "/fichero_texto_copia.txt"
os.remove(ruta_origen)
'''
# Comprobar si existe
import os.path

# print(os.path.abspath("../") )

if os.path.isfile(os.path.abspath("./" + "fichero_texto_copia.txt") ) == True:
    print(f"Existe el fichero ")
else:
    print("El ficheno NO existe")