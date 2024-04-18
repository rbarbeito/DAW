import sqlite3
import os

try:
    os.makedirs("dbase")
except FileExistsError:
    # directory already exists
    pass

##### Si no existe la bd la creamos si se conecta

##miConexion= sqlite3.connect("./dbase/PrimeraBBDD")
##miCursor=miConexion.cursor()
##
##miCursor.execute("CREATE TABLE productos (idProducto VARCHAR(10), Nombre_articulo VARCHAR(50), Precio INTEGER, Seccion VARCHAR(20), UNIQUE(idProducto))")
##
##
##print("Tabla creada correctamente.")



##miCursor.execute("INSERT INTO productos VALUES ('Balón', 25, 'Deportes')")

variosProductos=[
    ('art1','Camiseta', 10 ,'Deportes'),
    ('art2','Jarrón', 100,'Ceramica'),
    ('art3','Camión', 30,'Juguete'),
    ('art4','Gorra', 20 ,'Confecciones'),
    ('art5','PS5',2 ,'Juguete')
    ]

miCursor.executemany("INSERT INTO productos VALUES (?,?,?,?)", variosProductos)

##miCursor.execute("SELECT * FROM productos")
##
##productos=miCursor.fetchall()
##
##print(productos)
##
##for i in productos:
##    print(i[0], i[1], i[2], i[3])

miConexion.commit()
miConexion.close()
