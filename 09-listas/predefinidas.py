cantantes = ['2pac', 'Drake', 'Bad Buny', 'Julio Iglesias']
numeros = [1, 2, 5, 8, 3, 4, 6, 10, 7, 9]

# Ordenar
print(numeros)
numeros.sort()
print(numeros)

# añadir elementos

cantantes.append("Natos y Nastor")
cantantes.insert(1,"David Bisbal")
print(cantantes)

# Eliminar elementos
cantantes.pop(1)
cantantes.remove('Bad Buny')

# print(cantantes)

# Invertir orden
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('Drake' in cantantes)

# contar elementos
print(cantantes)
print(len(cantantes), "Cantantes en la lista")

# Cuantas veces aparece un elemento
numeros.append(8)
print( numeros.count(8) )

# Conseguir indice
print(cantantes.index("2pac"))

# Unir listas de diferentes tipos
cantantes.extend(numeros)
print(cantantes)