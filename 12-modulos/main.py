"""
Modulos: son funcionalidad ya hechas para reutilizar.
En Pyhton hay muchos modulos, lo puedes verificar en la documentacion de pyhton
https://docs.python.org/3/library/math.html?highlight=math#module-math
Podemo conseguir modulos que ya vienen en el lenguajel
modulos en internet, y tambien podemos crear nuestros modulos.
"""


# importar modulo propio
'''
import mimodulo
print(mimodulo.holaMundo("Victor Robles WEB")) 
print(mimodulo.funcionCalculadora() )
'''
# Modulo Fechas
import datetime
print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("Date: %d/%m/%Y, Time: %H:%M:%S")
print(fecha_personalizada)

print("**************** # Modulo Matematicas ********************* ")
# Modulo Matematicas
import math

print("Raiz cuadrada de 10: ", math.sqrt(25))
print("Numero pi: ", math.pi )
print("Redondear: ", math.floor(6.667989) )
print("Redondear: ", math.ceil(6.667989) )

# Modulo Random
import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15, 67) )


