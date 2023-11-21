# Comandos principales

1. `Truncate:` Vaciar el contenido de la base de datos
2. `Alter:` Editar la configuracion de la base de datos
3. `Create:` Crear la base datos, las tablas
4. `Drop:` Borrar contenido, tablas, o base de datos

## Tipos de datos

### Enteros

1. `int` o `integer` lo mismo que `2^32` 
2. `smallint` va desde -32768 a 32767
3. `tinyint` va desde -128 a 127
4. `mediumint` es `2^24`
5. `bigint` equivale a `2^64`

### Fixed Points (Excat Value)

1. Decimal
2. Numeric

## Float Points (Aproximate Value)

1. Float
2. Double
> Aqui hay que declararla precisión

`SysBD` - MySql

`SGBD` - Sistema de Gestion de base de datos

> Desde la CMD usamos le comando `mysql -u root -p` y nos permite loguiarnos al servidor de base de datos de mysql

![Loguiandonos en MySQL desde el CLI](image.png)

> Los comando de SQL todos terminan en `;`

> Limpiar la consola de mysql `system cls`

## Consulta en la base de datos

```SQL
SELECT user, host, plugin FROM mysql.user;
```

![Consulta a base de datos](image-1.png)

## Crear base de datos

```SQL
CREATE DATABASE <nombre>;
```

![Crear base de datos](image-3.png)
> En este comnado creamos una base de datos llamada `pepito`

## Ver databases en el servidor

```SQL
SHOW DATABASES;
```
![Mostrar bases de datos](image-4.png)


> Se puede acceder a cualquier tabla dentro de la base de datos usando la convencion del ``<nombre_de_la_tabla>.<campo>``

> Si se quiere trabajar en una sola base de datos se usa el comando `USE` para no tener que usar constantemente la convencion anterior

```SQL
USE pepito;
```

![Usando base de datos](image-5.png)

