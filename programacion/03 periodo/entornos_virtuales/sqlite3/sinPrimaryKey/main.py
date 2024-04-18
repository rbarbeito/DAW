import sqlite3

##### Si no existe la bd la creamos si se conecta

miConexion= sqlite3.connect("dbase/PrimeraBBDD")
miCursor=miConexion.cursor()

### miCursor.execute("CREATE TABLE productos (Nombre_articulo VARCHAR(50), Precio INTEGER, Seccion VARCHAR(20))")


##print("Tabla creada correctamente.")



####miCursor.execute("INSERT INTO productos VALUES ('Balón', 25, 'Deportes')")

##variosProductos=[
##    ('Camiseta', 10 ,'Deportes'),
##    ('Jarrón', 100,'Ceramica'),
##    ('Camión', 30,'Juguete'),
##    ('Gorra', 20 ,'Confecciones'),
##    ('PS5',2 ,'Juguete')
##    ]

##miCursor.executemany("INSERT INTO productos VALUES (?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM productos")

productos=miCursor.fetchall()

print(productos)

for i in productos:
    print(i[0], i[1], i[2])

##miConexion.commit()
miConexion.close()
