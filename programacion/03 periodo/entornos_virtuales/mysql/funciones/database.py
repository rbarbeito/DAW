from funciones.conection import conexion_db, create_cursor, close_cursor, close_cnx

def create_db(database):
    cnx = conexion_db()
    cursor = create_cursor(cnx)

    try:
        sql_Delete_database = "DROP DATABASE IF EXISTS " + database
        cursor.execute(sql_Delete_database)

        sql_CREATE_DB = "CREATE DATABASE " + database + \
            " CHARACTER SET utf8mb4 collate utf8mb4_general_ci"
        cursor.execute(sql_CREATE_DB)
    except Exception as e:
        print("Algo salio mal creando la database")
        print(e)

    close_cursor(cursor)
    close_cnx(cnx)


if __name__ == '__main__':
    print("Soy un modulo, no me ejecuto")