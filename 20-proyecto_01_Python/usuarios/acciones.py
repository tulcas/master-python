import usuarios.usuario as modelo
import notas.acciones 

class Acciones:

    def registro(self):
        print("\n OK. Vamos a registrarte en el sistema ... ")

        nombre = input(" Ingresar nombre: ")
        apellidos = input(" Ingresar apellido: ")
        email = input(" Ingresar su e-mail: ")
        passwd = input(" Ingresar su passwd: ")

        usuario = modelo.Usuario(nombre, apellidos, email, passwd)
        registro = usuario.registar()

        if registro[0] >= 1:
            print(f"\nEl usuario: {registro[1].nombre} se ha registrado con exito con el e-mail: {registro[1].email}")
        else:
            print("No te has registrado correctamente....")
    
    def login(self):
        print("Vale. Ingrese las credenciales...")

        try:
            email = input("Ingresa tu e-mail: ")
            passwd = input("Ingresa tu passwd: ")

            usuario = modelo.Usuario('', '', email, passwd)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido: {login[1]}, te has registrado en el sistema el: {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login Incorrecto intentar de nuevo mas tarde...")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        1. Crear nota
        2. Mostrar tus notas
        3. Eliminar nota
        4. Salir
              """)
        
        accion = int( input("Elige una opcion: ") )
        hazEl =  notas.acciones.Acciones()


        if accion == 1:
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == 2:
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == 3:
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == 4:
            print(f"\nOK {usuario[1]} hasta pronto")
            exit()