# Ejemplo 4
'''
print ("\n########################## EJEMPLO 4 ########################## ")



if dia == 1:
    print("Es Lunes") 
else:
    if dia == 2:
        print("Es Martes")
    else:
        if dia == 3:
            print("Es Miercoles")
        else:
            if dia == 4:
                print("Es Jueves")
            else:
                if dia == 5:
                    print("Es Viernes")
'''
'''
dia = int(input("Introduce el numero del dia de la semana: "))

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana")
'''

# Ejemplo 5
'''
print ("\n########################## EJEMPLO 5 ########################## ")

edad_oficial = int(input("Introduce la edad de la persona... "))

edad_minima = 18
edad_maxima = 65


if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Esta en edad de trabajar!")
else:
    print("No esta en edad de trabajar...")

'''

'''
# Ejemplo 6

print ("\n########################## EJEMPLO 6 ########################## ")

pais = "España"

if not( pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana !! ")
else:
    print(f"{pais} SI es un pais de habla hispana !! ")

    '''


# Ejemplo 8

print ("\n########################## EJEMPLO 8 ########################## ")

pais = "USA"

if  pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla hispana !! ")
else:
    print(f"{pais} SI es un pais de habla hispana :(  ")



