"""
Ejercicio 09
Crear un programa que pida numeros al usuario idefinidamente
hasta meter el numero 111
"""

contador = 1

while contador < 100 :
    print("Para terminar el programa ingrese: 111 ")
    num_input = int(input("Ingrese un valor : "))
    
    if num_input == 111:
        print("Fin del programa...")
        break
    else:
        print(f"Usted a ingresado: el numero: {num_input } ")