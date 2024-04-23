#!/usr/bin/env python3

import mysql.connector
import os
from dotenv import load_dotenv

# host = 'localhost'
# user = 'root'
# password = 'M@ripos4'


def conexion_db(db=None):

    load_dotenv()
    try:
        return mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            passwd=os.getenv('MYSQL_PASSWORD'),
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