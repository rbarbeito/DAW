DROP DATABASE IF EXISTS ejercicio_04;
CREATE DATABASE ejercicio_04 CHARSET utf8mb4 COLLATE utf8mb4_general_ci;
USE ejercicio_04;

CREATE TABLE clientes (
    dni VARCHAR(20) UNIQUE PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    apellidos VARCHAR(45) NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    telefono VARCHAR(25) NOT NULL
);

CREATE TABLE coches (
    matricula VARCHAR(25) UNIQUE PRIMARY KEY,
    modelo VARCHAR(20) NOT NULL,
    marca VARCHAR(20) NOT NULL,
    color VARCHAR(15) NOT NULL,
    dni_cliente VARCHAR(20),
    FOREIGN KEY (dni_cliente)
        REFERENCES clientes (dni)
);

CREATE TABLE mecanicos(
dni varchar(20) unique PRIMARY key,
nombre varchar(25) not null,
apellidos VARCHAR(45) not null,
contratado DATETIME not null default(current_timestamp()),
salario decimal(5,2) not null default(0.00)
);

create table mecanico_repara_coche(
id_reparacion int unsigned primary key,
dni_mecanico varchar(20) not null,
matricula_coche varchar(25) not null,
fecha datetime not null default(current_timestamp()),
horas_trabajo decimal(5,2) not null DEFAULT(0.00),
FOREIGN KEY(dni_mecanico) REFERENCES mecanicos(dni),
FOREIGN KEY(matricula_coche) REFERENCES coches(matricula)
);