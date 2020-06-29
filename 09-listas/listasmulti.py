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

# print(contactos[1][1] )

for i in contactos:
    for j in i:
        if i.index(j) == 0:
            print("Nombre: " + j)
        else:
            print("Email: " + j)
    print("\n")
