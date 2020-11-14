"""
Proyecto Python y Mysql
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un usuario en la BBDD
- Si elegimos login, indentifica al usuario y nos preguntara
- Crear nota, mostrar notas, borrarlas
"""
from usuarios import acciones


print("""
Acciones disponibles :
    - 1. Registro
    - 2. Login
""")
ejecutar = acciones.Acciones()

accion = int(input("Por favor ingresa una opocion - (Ingrese el numero correspondiente):  ") )
if accion == 1:
    ejecutar.registro()
    
elif accion == 2:
    ejecutar.login()
    


