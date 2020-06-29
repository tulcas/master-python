def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"

def funcionCalculadora():

    print( "########## CALCULADORA BASICA ##########" )
        
    print("Para SUMA igresa: 1")
    print("Para RESTA igresa :2 ")
    print("Para MULTIPLO igresa: 3")
    print("Para DIVISION igresa: 4")
    opcion = int(input("Ingrese una opcion:  "))

    print( "AHORA INGRESE LOS VALORES" )
    num1 = int(input("Ingresa un valor: "))
    num2 = int(input("Ingresa otro valor: "))

    if opcion == 1:
        
        return (print(f"La SUMA de ambos numeros es: {num1 + num2}") )
    elif opcion == 2:
        return (print(f"La RESTA de ambos numeros es: {num1 - num2}") )
    elif opcion == 3:
        return (print(f"El MULTIPLO de ambos numeros es: {num1 * num2}") )
    elif opcion == 4:
        return (print(f"La DIVISION de ambos numeros es: {num1 / num2}") )
    else:
        return (print("Fin de calculadora") )
