from tkinter import *

ventana = Tk()
#ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
            fg="white",
            bg="black",
            padx=50,
            pady=20,
            font=("Consolas", 30)
)
texto.pack(side=TOP)

texto = Label(ventana, text="Soy Victor Robles")
texto.config(
    height=3,
    bg="orange",
    font=("Arial", 20),
    padx=10,
    pady=20,
    cursor="watch"

)
texto.pack(side=TOP, fill=X, expand=YES )



texto = Label(ventana, text="Basico 1" )
texto.config(
    height=3,
    bg="green",
    font=("Arial", 20),
    padx=10,
    pady=20,
    cursor="watch"

)
texto.pack(side=LEFT, fill=X, expand=YES )


texto = Label(ventana, text="Basico 2" )
texto.config(
    height=3,
    bg="red",
    font=("Arial", 20),
    padx=10,
    pady=20,
    cursor="watch"

)
texto.pack(side=LEFT, fill=X, expand=YES )

texto = Label(ventana, text="Basico 3" )
texto.config(
    height=3,
    bg="pink",
    font=("Arial", 20),
    padx=10,
    pady=20,
    cursor="watch"

)
texto.pack(side=LEFT, fill=X, expand=YES )



ventana.mainloop()

