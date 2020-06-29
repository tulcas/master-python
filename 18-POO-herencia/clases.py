# HERENCIA: Es la posibilida de compartir atributos y metodos
# entre cases. Y que diferentes clases hereden de otras

class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """
    #getters
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura

    def getEddad(self):
        return self.edad
    #Setters
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    
    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"
    
class Informatico(Persona):
    """
    lenguajes
    experiencia
    """
    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScritp, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy Programando"

    def repararPC(self):
        return "He reparado tu Ordenador"

class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__() ## Para tenes acceso a la clase padre y sus valores
        self.auditarRedes = 'Experto'
        self.experienciaRedes = 15

    def aufitoria(self):
        return "Estoy auditando una red"