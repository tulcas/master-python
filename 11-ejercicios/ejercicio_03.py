"""
Ejercicio. 3

Programa que compruebe si una variable esta vacia, rellenarla con texto en minusculas
y mostrarlo en mayuculas.

"""

# variable
texto = ""
'''
if texto == "":
    texto = input(f"El contenido de la variable es: {texto} esta vacia ingresa un valor:  ")
    print(f"El contenido de la variable ahora es: {texto} ")
    print(f"El dato ingresado en Minusculas es: {texto.lower() }")
    print(f"El dato ingresado en Mayusculas es: {texto.upper() }")
'''
if len(texto.strip() ) <= 0:
    texto = input(f"El contenido de la variable en este momento es NULL ingresa un valor:  ")
    print(f"El contenido de la variable ahora es: {texto} ")
    print(f"El dato ingresado en Minusculas es: {texto.lower() }")
    print(f"El dato ingresado en Mayusculas es: {texto.upper() }")
else:
        print(f"La variable tiene el siguiente contenido: {texto}")
