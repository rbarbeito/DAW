#!/usr/bin/env python3
from funciones.conection import conexion_db, create_cursor, close_cursor, close_cnx



from faker import Faker
fake = Faker()


def dataRnd(db, cantidad: int = 10):
    cnx = conexion_db(db)
    cursor = create_cursor(cnx)

    try:
        data = []
        sql = "INSERT INTO users VALUES (%s,%s,%s,%s,%s) "
        for i in range(cantidad):
            my_tupla = (None, fake.first_name(), fake.last_name(),
                        fake.ascii_company_email(), fake.password(length=40))
            data.append(my_tupla)

        cursor.executemany(sql, data)

        cnx.commit()

        print("\nDatos random insertados con exito")

    except Exception as e:
        print("Algo ocurrió con la inserción de datos")
        print(e)

    close_cursor(cursor)
    close_cnx(cnx)


if __name__ == "__main__":
    print("soy un modulo")
