from tkinter import *

ventana = Tk()
ventana.title("Marcos | Master en Python ")
ventana.geometry("700x700")

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue",
    bd=5,
    relief=SOLID
)
marco_padre.pack(side=BOTTOM, fill=X, expand=YES )


marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=5,
    relief=SOLID

)
marco.pack(side=LEFT, anchor=SW)


marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd=5,
    relief=SOLID

)
marco.pack(side=RIGHT, anchor=SW)


marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue",
    bd=5,
    relief=SOLID
)
marco_padre.pack(side=TOP, fill=X, expand=YES )
ventana.mainloop()

