"""
# BUCLE WHILE
Estructura de control que itera o repite  la ejecucion de una serie de instrucciones
tantas veces como sea necesario hasta que deje de cumplrise la condicion.

codigo:

while $condicion:
    bloque de instrucciones
    //contador
"""




contador = 1

while contador <= 10:
    print(f"Mostrando numero: {contador}")
    contador = contador + 1
  

print("-------------------------------------------")
contador = 1
muestrame = str(0)

while contador <= 10:
    muestrame = muestrame + ", " + str(contador)
    contador = contador + 1    
print(muestrame)

# Ejemplo

print("#### EJEMPLO #### ")
numero_usuario = int(input("De que numero quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla del {numero_usuario}")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador}  = {numero_usuario*contador}")
    contador += 1
else:
    print("Tabla Terminada....")



