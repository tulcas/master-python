"""

Variables locales: Se definen dentro de la funciojn y no se puede user fuera de ella,
solo estan disponibles dentro.
A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una funcion
y estan disponibles dentro y fuera de ellas.


"""

# Variable global 

frase = "Ni los genios son tan genios, ni los mediocres son tan mediocres"

print(frase)
year = 2020

def holaMundo():
    frase = "Hola Mundo!!! "
    print("Dentro de la funcion")
    print(frase)

    year = 2021
    print(year)

    # Asi se declara una Variable Global
    global website 
    website = "victorroblesweb.es"
    print("Dentro de la funcion", website)

holaMundo() 
print(year)

print("Fuera de la Funcion: ", website)