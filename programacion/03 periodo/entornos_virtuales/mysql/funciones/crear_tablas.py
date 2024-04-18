from funciones.conection import conexion_db, create_cursor, close_cursor, close_cnx


def createTable(db):
    sql="""CREATE TABLE users (
        id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(30),
        apellidos VARCHAR(30),
        email VARCHAR(100) UNIQUE,
        password VARCHAR(255)
    );"""

    cnx = conexion_db(db)
    cursor = create_cursor(cnx)

    try:
        cursor.execute(sql)
    except Exception as e:
        print("No se pudo crear la Tabla")
        print(e)

    close_cursor()
    close_cnx()























if __name__ == "__main__":
    print("Soy un modulo")