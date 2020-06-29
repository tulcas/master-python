# Importar Modulo
import sqlite3

# Conexion a base de datos
conexion = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear Tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo varchar(255),  
descripcion TEXT,  
precio int(255) 
);
""")

# Guardar cambios
conexion.commit()

# Insertar Datos
cursor.execute("INSERT INTO productos VALUES (null, 'PRIMER producto', 'Descriptcion de mi producto', 550)")
conexion.commit()

# Borrar Registros
cursor.execute("DELETE FROM productos")
conexion.commit()



#  Insertar muchos registro de golpe
productos = [
    ("Ordenador Portatil", "Acer gamer PRO", 700 ),
    ("Telefono Movil", "One PLUS gamer PRO", 80 ),
    ("MotherBoard", "Acer ASPIRE PRO", 850 ),
    ("TABLET 15", " gamer PRO", 300 ),
]

cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80 ")


# Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 300; ")
print(cursor)
productos = cursor.fetchall()

for i in productos: 
    print("ID: ", i[0])
    print("titulo: ", i[1])
    print("descripcion:", i[2])
    print("precio:", i[3])
    print("\n")

cursor.execute("SELECT TITULO FROM productos; ")
i = cursor.fetchone()
print(i)



# Cerrar Conexion
conexion.close()


