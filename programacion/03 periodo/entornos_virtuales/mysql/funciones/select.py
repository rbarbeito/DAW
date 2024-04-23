from funciones.conection import conexion_db,create_cursor,close_cursor,close_cnx


def selectByName(db,dt):

    cnx=conexion_db(db)
    cursor=create_cursor(cnx)

    try:

        sql="SELECT CONCAT(nombre,' ',apellidos )as nombre, email from users where nombre like '%?%'"
        cursor.execute(sql)
        data=cursor.fetchall()
        return data

    except Exception as e:
        print("Ocurrió algun error en la consulta selectByName")
        print(e)

    close_cursor(cursor)
    close_cnx(cnx)



def selectByLastName(db,dt):

    cnx = conexion_db(db)
    cursor = create_cursor(cnx)

    try:

        sql = "SELECT CONCAT(nombre,' ',apellidos )as nombre, email from users where apellidos like '%?%'"
        cursor.execute(sql,(dt,))
        data = cursor.fetchall()
        return data

    except Exception as e:
        print("Ocurrió algun error en la consulta selectByLastName")
        print(e)

    close_cursor(cursor)
    close_cnx(cnx)



def selectByEmail(db,dt):

    cnx = conexion_db(db)
    cursor = create_cursor(cnx)

    try:

        sql = "SELECT CONCAT(nombre,' ',apellidos )as nombre, email from users where email like '%?%'"
        cursor.execute(sql,(dt,))
        data = cursor.fetchall()
        return data

    except Exception as e:
        print("Ocurrió algun error en la consulta selectByEmail")
        print(e)

    close_cursor(cursor)
    close_cnx(cnx)


def selectAllPagination(db,pagination):

    cnx = conexion_db(db)
    cursor = create_cursor(cnx)

    try:

        sql = "SELECT CONCAT(nombre,' ',apellidos )as nombre, email from users"
        cursor.execute(sql)
        data = cursor.fetchmany(pagination)
        return data

    except Exception as e:
        print("Ocurrió algun error en la consulta selectByEmail")
        print(e)

    close_cursor(cursor)
    close_cnx(cnx)



if __name__ == "__main__":
    print("Soy un módulo")

    