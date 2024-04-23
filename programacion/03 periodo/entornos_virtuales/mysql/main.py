import os
from dotenv import load_dotenv

from funciones.database import create_db
from funciones.crear_tablas import createTable
from funciones.create_data import dataRnd
from funciones.select import selectByName, selectByLastName, selectByEmail, selectAllPagination

load_dotenv()
db = os.getenv('MYSQL_DB')

list_menu = [
    ("INICIAR o RESETEAR Database","cDb"),
    ("Selecccionar por nombre","sN"),
    ("Seleccionar por apellido","sA"),
    ("Seleccionar por email","sE"),
    ("Listar usuarios paginados","lUP"),
    ("Insertar nuevo","iN"),
    ("Borrar por id","bI"),
]
long = 0
for i in list_menu:
    if long < len(i[0]):
        long = len(i[0])

long+=8


while True:

    print()
    print("*"*(long))
    print(" "*((long-len("Menú"))//2), "Menú", sep="")
    print("*"*(long))
    print()

    for i in range(len(list_menu)):
        print(" "*2, i+1, ". ", list_menu[i][0],  sep="")

    print(" "*2, "0. Salir",  sep="")
    print()
    print("*"*(long))
    seleccion = input("\n¿Qué acción desea realizar: ")

    try:
        if seleccion!="0":
            menu = list_menu[int(seleccion) - 1][1]
        else:
            menu=int(seleccion)

    except ValueError:
        print("Acción no valida") 
        continue

    if menu == "cDb":
        create_db(db)
        createTable(db)
        dataRnd(db, 100)

    if menu == "sN":
        name= input("Nombre a buscar: ")
        users= selectByName(db,name)

        if len(users)==0:
            print("No tenemos registrado ese usuario")
            continue

        print("Usuarios encontrados: ", len(users))
        print()
        print("Usuarios")
        print("Nombre", "Email")
        for user in users:
            print(user[0], user[1] )

    if menu == "sA":
        lastName= input("Apellido a buscar: ")
        users= selectByLastName(db,lastName)

        if len(users)==0:
            print("No tenemos registrado usuario con ese apellido")
            continue

        print("Usuarios encontrados: ", len(users))
        print()
        print("Usuarios")
        print("Nombre", "Email")
        for user in users:
            print(user[0], user[1] )
            
    if menu == "sE":
        email= input("Email a buscar: ")
        users= selectByEmail(db,email)

        if len(users)==0:
            print("No tenemos registrado usuario con ese correo")
            continue

        print("Usuarios encontrados: ", len(users))
        print()
        print("Usuarios")
        print("Nombre", "Email")
        for user in users:
            print(user[0], user[1] )
            
        if menu == "lUP":
            while True:
                paginacion= input("Cuantos resultados quiere en cada respuesta: ")

                try:
                    paginacion=int(paginacion)

                    if paginacion <= 0:
                        print("Solo se aceptan valores mayores que 1")
                        continue

                    break

                except Exception as e:
                    print("Solo se aceptan números")
                    continue

        users= selectAllPagination(db,paginacion)

        if users==None:
            print("No tenemos registrado usuario con ese correo")
            continue

        print("Usuarios encontrados: ", len(users))
        print()
        print("Usuarios")
        print("Nombre", "Email")
        for user in users:
            print(user[0], user[1] )


    elif menu == 0:
        break
    else:
        print("Acción no definida")
        continue


print("Hasta la vista Baby!!")
