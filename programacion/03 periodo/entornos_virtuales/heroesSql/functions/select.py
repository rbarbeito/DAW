#!/usr/bin/env python3

from functions.conection import conexion_db, create_cursor, close_cursor, close_cnx

def selectAll():

    cnx = conexion_db()
    cursor = create_cursor(cnx)

    try:
        sql = "SELECT * from superheroes"
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    except Exception as e:
        print("Ocurrió algun error en la consulta selectByName")
        print(e)

    close_cursor(cursor)
    close_cnx(cnx)
