from coche import Coche

carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Coche("Verde", "SEAT", "PANDA", 240, 200, 4)
carro2 = Coche("Azul", "Citroen", "XARA", 100, 180, 4)
carro3 = Coche("Rojo", "Mercedez", "Clase A", 350, 400, 4)

'''
print( carro.getInfo())
print( carro1.getInfo())
print( carro2.getInfo())
print( carro3.getInfo())
'''
carrosTodos = [carro.getInfo(), carro1.getInfo(), carro2.getInfo(), carro3.getInfo()]

contador = 0
for i in carrosTodos:
    
    print(f" ---------- Detalle de carro numero:{contador} ---------- {i} ")
    contador += 1

# Detectar tipado
# carro3 = bool
if type(carro3) == Coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto!!")

# Visibilidad
print(carro.variable_publica)
print(carro.getVariablePrivada() )