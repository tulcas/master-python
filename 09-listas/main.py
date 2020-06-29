"""
LISTAS (ARRAYS)
Son colecciones o conjuntos de datos/valores, bajo un unico
nombre.

Para acceder a esos valores podemos usar un indice numerico.

"""

pelicula = "Batman"

# Definir lista
peliculas = ["Batman", "SpiderMAN", "The lord Of the rings"]

cantantes = list( ('2pac', 'Drake', 'Jennifer Lopez') )
years = list(range(2020, 2030) )
variada = ["Victor", 30, 4.4, True, "Texto"]

'''
print(pelicula)
print(peliculas)
print(cantantes)
print(years)
print(variada)
'''

# Indices

print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[0:])
peliculas[-2] = "IronMan"
print(peliculas[0:])

# Añadir elementos a una lista

cantantes.append("Kase O")
cantantes.append("Natos y Waor")

print(cantantes)


# Recorrer Lista
print( "\n********************* Listado de Peliculas *****************************" )

nueva_pelicula = " "
while nueva_pelicula != "parar":
    nueva_pelicula = input("Ingresa el nombre de la pelicula: ")
    
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for i in peliculas:
    print(f"{ peliculas.index(i)+1 }. es : {i}")


# Listas multidimensionales

print( "\n ************** Lista de contactos **************" )
contactos = [
    [
        'Antonio',
        'antonio@gmail.com' 
    ],
    [
        'Luis',
        'luis@gmail.com'
    ],
    [
        'Salvador',
        'salvador@gmail.com'
    ]

]