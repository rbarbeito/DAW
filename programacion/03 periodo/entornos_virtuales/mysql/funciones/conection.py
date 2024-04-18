import mysql.connector
host = 'localhost'
user = 'root'
password = 'M@ripos4'


def conexion_db(db=None):
    try:
        return mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=db)
    except Exception as e:
        print("Error de conexion")
        print(e)


def create_cursor(cnx):
    try:
        return cnx.cursor(prepared=True)
    except Exception as e:
        print("Algo salio mal en el conector")
        print(e)


def close_cursor(cursor):
    cursor.close()

def close_cnx(cnx):
    cnx.close()


if __name__ == '__main__':
    print("Soy un modulo, no me ejecuto")