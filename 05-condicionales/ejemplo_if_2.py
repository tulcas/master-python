# Ejemplo 3

print ("\n########################## EJEMPLO 3 ########################## ")

nombre = "Victor Robles"
ciudad = "Barcelona"
continente = "Europa"
edad = 17
mayoria_de_edad = 18

if edad >= mayoria_de_edad:
    print(f"{nombre} es mayor de edad!!")
    if continente != "Europa":
        print(f"{nombre} NO es Europeo, vive en {continente}")
    else:
        print(f"{nombre} Es Europeo, y vive en {ciudad}")
else:
    print(f"{nombre} NO es mayor de edad")
    if continente != "Europa":
        print(f"{nombre} NO es Europeo, vive en {continente}")
    else:
        print(f"{nombre} Es Europeo, y vive en {ciudad}")