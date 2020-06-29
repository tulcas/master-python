"""
# FOR
for variable in elemento iterable
    BlOQUE DE INSTRUCCIONES
"""
'''
contador = 0
resultado = 0

for contador in range(0, 10):
    print ("Voy por el " + str(contador))

    resultado += contador

print(f"el resultado: es {resultado}")
'''
# Ejemplo de tablas de multiplicar

numero_usuario = int(input("De que numero quieres la tabla ?: "))

if numero_usuario <= 1:
    numero_usuario = 1

print(f"#### Tabla de multiplicar del numero {numero_usuario} ####")

for numero_tabla in range(1, 11):

    if numero_usuario == 45:
        print("No se pueden mostrar numero prohibidos !!!")
        break

    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla Finalizada...")
  

