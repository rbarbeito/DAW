# Trabajo con usuarios

```SQL
-- Create usuario
mysql> CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';

-- Garantizar privilegios de un usuario a la base de datos
mysql> GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';

-- Cambios tengan efecto
mysql> FLUSH PRIVILEGES;

--Crear otro super usuario
mysql> GRANT ALL PRIVILEGES ON *.* TO 'username'@'%';
```

## Garantizar privilegios personalizados

```SQL

-- Garantiza todos los derechos a Jeffrey en todas las tablas de la base de datos db1, siempre que se conecte desde localhost
GRANT ALL ON db1.* TO 'jeffrey'@'localhost';

-- Se crea el role1 que solo permite leer en las tablas de la base de datos world
-- Garantiza el role1 y role2 a los user1  y user2 siempre que se conecten desde localhost
GRANT SELECT ON world.* TO 'role1';
GRANT 'role1', 'role2' TO 'user1'@'localhost', 'user2'@'localhost';


-- El usuario jeffrey solo puede realizar un total de 90 queries en una hora, autenticado en localhost
ALTER USER 'jeffrey'@'localhost' WITH MAX_QUERIES_PER_HOUR 90;

--Mostrar los permisos de un usuario determinado
SHOW GRANTS FOR jeffrey;

--Revocar los permisos
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user'@'localhost';
```

## Listar Bases de datos
```SQL
SHOW DATABASES;
```
 