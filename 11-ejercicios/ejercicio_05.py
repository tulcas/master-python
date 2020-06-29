"""
Ejercicio 5.

Crear una lista con el contenido de esta tabla:



"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA","COD","PUB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["Assassin´s Creed", "CRASH", "Prince of Persia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for i in tabla:
    print(f"Catergoria del juego ********************* {i['categoria']} ********************* ")
    for j in i['juegos']:
        print(j)