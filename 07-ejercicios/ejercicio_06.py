"""
# Ejercicio 06
Mostrar todas las tablas de Multiplicar del 1 al 10
Mostrando el titulo de la tabla y luego las multiplicaciones
"""

for cabecera in range(1, 11):
    print("########################################")
    print(f"############ Tabla del {cabecera} ############ ")
    print("########################################")

    for numero in range(1, 11):
        print(f"{numero} X {cabecera} = {numero * cabecera}")
    
    print("\n")