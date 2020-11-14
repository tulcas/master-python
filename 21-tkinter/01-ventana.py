# tkinter
# Modulo para crear interfaces graficas de usuario

from tkinter import *
from tkinter import Tk
from tkinter import *
from tkinter import *
from platform import system
from platform import system

# Crear la ventana RAIZ



ventana = Tk()

# Titulo de la ventana
ventana.title("Interfaz grafica con python")

# Incono de la ventana


ventana.iconbitmap("/Users/andres/Documents/master-python/21-tkinter/imagenes/logotest.icns")

#cambiar tamanio ventana
ventana.geometry("750x450")

#bloquear tamanio de la ventana
ventana.resizable(0, 0)

# Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()
