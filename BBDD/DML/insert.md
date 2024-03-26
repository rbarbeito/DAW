## DML INSERT

```SQL
-- Formato de la instruccionn
INSERT INTO <tabla> (campo1, campo2, campo3) VALUES(val1, val2, val3);
```

```SQL
-- ojo con esto
INSERT INTO <tabla> () VALUES (val1, val2, val3 .....)
-- Si hacemos esto estamos diciendo que vamos adicionar todos los campos de la tabla, si la misma tiene 4 campos, debemos colocar 4 valores en `VALUES`
```

> No hace falta poner datos que columnas que aceptan valores nulos por defecto, al igual que las columnas que tienen valores autoincrementales

Cuando queremos insertar varios registros se hace de esta manera

```SQL
-- Formato de la instruccionn
INSERT INTO <tabla> (campo1, campo2, campo3) 
VALUES(val1, val2, val3),
(val1, val2, val3),
(val1, val2, val3),
(val1, val2, val3),
(val1, val2, val3),
(val1, val2, val3);
```

> 📝 Con el insert solo vamos a tener problemas con la adición que ya registros que su primary key se encuentre en la tabla

```sql
# Prepared statement
prepare stmt1 from 'Select sqrt(pow(?,2)+pow(?,2)) as HYPOTENUSE';
SET @a=3;
SET @b=4;

execute stmt1 using @a,@b;
deallocate prepare stmt1;


```

```sql
# Prepare statment para seleccionar todos los datos de una tabla
Set @table="usuarios";
set @s=CONCAT('select * from ', @table);

Prepare stmt2 from @s;
execute stmt2;
```

```sql
# Prepare statment for insert data
prepare stmt3 from 'insert into usuarios(nombre,apellidos,edad,fecha_nacimiento,email) values(?,?,?,?,?)';
set @nombre="Ruperto";
set @apellido="manguera";
set @edad=25;
set @fecha="1986-01-28";
set @email="camaleon@camaleon.com";
execute stmt3 using @nombre,@apellido,@edad,@fecha,@email;
```