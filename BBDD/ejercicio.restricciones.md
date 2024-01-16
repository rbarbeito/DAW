# Restricciones

```SQL
DROP DATABASE IF EXISTS pruebas_integridad;
CREATE DATABASE pruebas_integridad CHARSET utf8mb4 COLLATE utf8mb4_general_ci;
USE pruebas_integridad;

CREATE TABLE usuarios (
    idusuario INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    edad TINYINT UNSIGNED,
    correo VARCHAR(150)
);

CREATE TABLE curso (
    idcurso INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    asignatura VARCHAR(100),
    capacidad SMALLINT UNSIGNED,
    idusuario INT UNSIGNED,
    FOREIGN KEY (idusuario)
        REFERENCES usuarios (idusuario)
);
```

## Con las relaciones de manera restrictiva

```SQL
use pruebas_integridad;

DELETE FROM usuarios WHERE idusuario = '1';
```

> **Respuesta:** Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`pruebas_integridad`.`curso`, CONSTRAINT `curso_ibfk_1` FOREIGN KEY (`idusuario`) REFERENCES `usuarios` (`idusuario`))


## Con las relaciones de manera CASCADE

> :sound: **`ON UPDATE CASCADE`** => Actualiza el valor de las claves foráneas cuando se actualiza la `PK` a la que hace referencia

> :sound: **`ON DELETE CASCADE`** => Borra el valor de las claves foráneas cuando se actualiza la `PK` a la que hace referencia

## Con las relaciones de manera SET NULL

> :sound: Actualiza el valor de las claves foráneas situándolas a `null`


## Con las relaciones de manera NO ACTION

> :sound: Funciona de manera restrictiva en la version Mysql 8.0


## Create User

```SQL
CREATE USER 'nombre'@'ip_maquina' IDENTIFIED BY '<password>';

CREATE USER 'nombre'@'ip_maquina' IDENTIFIED WITH '<plugins>' BY '<password>';
```

> :sound: **Ip_maquina** 
> - localhost
> - %
> - IP Maquina especifica

> :sound: **Plugins** 
> - caching_sha2_password
> - mysql_native_password
> - auth_socket

