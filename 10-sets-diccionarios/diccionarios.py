"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json.

"""

persona = {
    "nombre" : "Victor",
    "apellidos" : "Robles",
    "web": "victorroblesweb.es"
}

print(type(persona))
print(persona["web"] )

# Lista con diccionarios


print("\n \n \n \n ************************************************ ")

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@gmail.com'
    },
    {
        'nombre': 'Luis',
        'email': 'Luis@gmail.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@gmail.com'
    }
]

print(contactos[0]['nombre'])

print("\nListado de Contactos:")

for i in contactos:
    print("-----------------------------------")
    print(f"Nombre del contacto: {i['nombre']}")
    print(f"e-mail del contacto: {i['email']}")
    print("-----------------------------------")