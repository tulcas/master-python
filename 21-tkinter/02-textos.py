from tkinter import *

ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa...")
texto.config(
            fg="white",
            bg="black",
            padx=500,
            pady=20,
            font=("Consolas", 30)
)
texto.pack()

texto = Label(ventana, text="Soy Victor Robles")
texto.config(
    height=3,
    bg="orange",
    font=("Arial", 20),
    padx=10,
    pady=20,
    cursor="watch"

)
texto.pack(anchor=SE)

def pruebas(nombre, apellidos, pais):
    return f"Hola, {nombre} {apellidos}, veo que eres de: {pais}"

texto = Label(ventana, text=pruebas("Victor", "Robles", "España") )
texto.config(
    height=3,
    bg="green",
    font=("Arial", 20),
    padx=10,
    pady=20,
    cursor="watch"

)
texto.pack(anchor=NW)


ventana.mainloop()

