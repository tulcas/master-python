import os
import shutil
# Crear carpeta
'''
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("El direcotio ya existe...")

# Borrar carpeta
#os.rmdir("./mi_carpeta")

# copiar carpeta

ruta_origen = "./mi_carpeta"
ruta_destino = "./mi_carpeta_COPIA"

shutil.copytree(ruta_origen, ruta_destino)

# Eliminar carpeta
#os.rmdir("./mi_carpeta_COPIA")
'''
# Listar 

print("Contenido mi carpeta: ")
contenido = os.listdir("./mi_carpeta")

for i in contenido:
    print(i)