import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectardb()
database = connect[0]
cursor = connect[1]



class Usuario:

    def __init__(self, nombre, apellidos, email, passwd):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.passwd = passwd

    def registar(self):
        fecha = datetime.datetime.now()

        # Cifrar passwd
        cifrado = hashlib.sha256()
        cifrado.update(self.passwd.encode('utf8'))


        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try: 
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result
       

        return [cursor.rowcount, self]

    def identificar(self):


        # Consulta existencia de usuario
        sql =  "SELECT * FROM usuarios WHERE email = %s AND passwd = %s "

        # Cifrar passwd
        cifrado = hashlib.sha256()
        cifrado.update(self.passwd.encode('utf8'))

        usuario = (self.email, cifrado.hexdigest() )

        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest() )

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result


