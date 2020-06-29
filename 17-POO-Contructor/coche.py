# Programacion orientada a objetos (POO o OOP)
# Definir una clase (molde para crear mas objetos de ese tipo)
# (Coche) con caracteristicas similares 
class Coche:

    # Atributos o propiedades (variables)
    # caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    variable_publica = "Hola, soy un atributo publico"
    __variable_privada = "Hola, soy un atributo privado"

    def getVariablePrivada(self):
        return self.__variable_privada

    #inicializar constructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.caballaje = caballaje
        self.plazas =  plazas

    # Metodos, son acciones que hace el objeto (coche) (Conocidas como funciones)

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color 

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):

        info = f" "
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str( self.getVelocidad() )

        return info
        
    
# fin definicion clase

# Crear objeto // Instanciar clase
'''
coche = Coche()

coche.setColor("Amarillo")
coche.setModelo("Murcielago")

print("COCHE 1:")

print(coche.marca, coche.getModelo(), coche.getColor() )

print("Velocidad actual: ", coche.getVelocidad() )
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

coche.frenar()
print("Velocidad nueva: ", coche.velocidad )

# Crear mas objetos.



coche2 = Coche()

coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print("------------------------------")
print("COCHE 2:")

print(coche2.marca, coche2.getModelo(), coche2.getColor() )
print("Velocidad actual: ", coche2.getVelocidad() )
print(type(coche2))
'''