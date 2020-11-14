import notas.nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f"OK, {usuario[1]} !! vamos a crear una nueva nota...")
        titulo = input("Ingresa el titulo de tu nota: ")
        descripcion = input("Ingresa el contenido de tu nota:")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo} ")
        
        else:
            print(f"\nNo se ha guardado la nota: {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]} !! Aqui tienes tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for i in notas:
            print("***********************************************")
            print(i[2])
            print(i[3])

    def borrar(self, usuario):
        print(f"\n Okey {usuario[1]} !! vamos a borrar notas... ")

        titulo = input("Ingresa el titulo de la nota a boorar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("No se ha borrado la nota...,. intentalo de nuevo")















