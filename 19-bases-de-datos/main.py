import mysql.connector

# Conexion
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    port = "8889",
    database = "master_python"
)

# Conecto ok
# print(database)

# Cursos permite ejecutar consultas
cursor = database.cursor(buffered=True)

# Crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for i in cursor:
    print(i)
"""
# Crear Tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500 )")
#database.commit()


coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedez', 'Clase C', 35000)
]

# cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches )

database.commit()


# listar

cursor.execute("SELECT * FROM VEHICULOS    ")
result = cursor.fetchall()

print("---------- TODOS MIS COCHES --------")

for i in result:
    print( i[1], i[2], i[3] )

# Mostrar uno
cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)

# Borrar
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renault' ")
database.commit()

print(cursor.rowcount, "borrados !!")

# Actualizar
cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE marca='Seat' ")
database.commit()

print(cursor.rowcount, "Actualizados !!")