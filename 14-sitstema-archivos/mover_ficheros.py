from io import open
import pathlib
import shutil


# Mover

ruta_origen = str( pathlib.Path().absolute() ) + "/fichero_texto.txt"
ruta_destino = str( pathlib.Path().absolute() ) + "/fichero_texto_movido.txt"
 
shutil.move(ruta_origen, ruta_destino) 

