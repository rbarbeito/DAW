import sqlite3
import os

try:
    os.makedirs("dbase")
except FileExistsError:
    # directory already exists
    pass

##### Si no existe la bd la creamos si se conecta

miConexion= sqlite3.connect("./dbase/database")
miCursor=miConexion.cursor()
##
##miCursor.execute("CREATE TABLE productos (idProducto INTEGER PRIMARY KEY AUTOINCREMENT, Nombre_articulo VARCHAR(50), Precio INTEGER, Seccion VARCHAR(20))")
##
##
##print("Tabla creada correctamente.")
##
##
##
##variosProductos=[
##    ('Camiseta', 10 ,'Deportes'),
##    ('Jarrón', 100,'Ceramica'),
##    ('Camión', 30,'Juguete'),
##    ('Gorra', 20 ,'Confecciones'),
##    ('PS5',2 ,'Juguete')
##    ]
##
##miCursor.executemany("INSERT INTO productos VALUES (NULL,?,?,?)", variosProductos)

##miCursor.execute("SELECT * FROM productos")
##
##productos=miCursor.fetchall()
##
##print(productos)
##
##for i in productos:
##    print(i[0], i[1], i[2], i[3])


####miCursor.execute("select * from productos")
####
####producto = miCursor.fetchone()
####print(producto)
####
####producto = miCursor.fetchone()
####print(producto)


miCursor.execute("select * from productos where seccion='Ceramica'")

producto = miCursor.fetchall()
print(producto)


miConexion.commit()
miConexion.close()
