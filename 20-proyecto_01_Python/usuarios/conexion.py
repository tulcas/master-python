import mysql.connector

def conectardb():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "root",
        port = "8889",
        database = "master_python"
    )
    
    cursor = database.cursor(buffered=True)

    return [database, cursor]
