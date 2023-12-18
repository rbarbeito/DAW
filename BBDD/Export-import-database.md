# Dump database 😣

```MYSQL
mysqldump -u root -p <database> > <archivo_a_crear.sql>
```

Esto lo guarda en la carpeta donde se este ejecutando en `command cli`


## Exportar todas las base de datos de tu server 🤔

```MYSQL
mysqldump -u root -p -alldatabases > <archivo_a_crear.sql>
```


`change`  Renombrar columna, cambia tipos de datos u Ambos

`modify` Modificar tipos de datos

`rename` renombrar columna, renombrar table

### Alter de tablas

```SQL
-- Rename (las 2 formas de hacerlo)
 ALTER TABLE categoria RENAME categoria_buena;
 RENAME TABLE categoria_buena TO categoria;
```

```SQL
-- adcionar columna 
--Se pueden adicionar todas las columnas que se neceiten de una sola vez
ALTER TABLE categoria ADD COLUMN pais_origen3 VARCHAR(100), ADD COLUMN pais_origen VARCHAR(200);

-- Añade en primera posición de la tabla
ALTER TABLE categoria ADD COLUMN fecha DATE FIRST; 

-- Adiciona una nueva columna despues de l columna pais_origen
ALTER TABLE categoria ADD COLUMN fecha2 DATE AFTER pais_origen; 
```


```SQL
-- CHANGE 
-- Cambiar nombre columna, tipos de datos o ambos
-- Para cambiar solo el nombre es importante poner tambien el tipo de dato en la instrución
ALTER TABLE categoria CHANGE COLUMN fecha fechita DATETIME;
ALTER TABLE categoria CHANGE COLUMN fechita fecha DATETIME;
ALTER TABLE categoria CHANGE COLUMN fecha DATE;
```

```SQL
-- MODIFY
-- Modificart ipos de datos de una columna
ALTER TABLE categoria MODIFY pais_origen CHAR(50) NOT NULL;
```

```SQL
-- DROP
-- Borrar columna, table o bases de datos
ALTER TABLE categoria DROP COLUMN fecha;
-- se puede borrar varias columnas a la vex
ALTER TABLE categoria DROP COLUMN pais_origen3, DROP COLUMN pais_origen, DROP COLUMN fecha2;
```

```SQL
--  Deshabilitar verificacion de llaves foraneas
SET FOREIGN_KEY_CHECKS=0;
--  Borrar, truncar tablas necesarias
DROP TABLE categoria;
-- Habilitar la verificacion de llaves foraneas
SET FOREIGN_KEY_CHECKS=1;
```

```SQL
-- Borrar la Base de datos
-- Se puede usar cualquiera de las 2 sentencias
DROP SCHEMA ex01;
DROP DATABASE ex01;
```