DROP DATABASE IF EXISTS ejercicio_01;
CREATE DATABASE ejercicio_01 CHARSET utf8mb4 COLLATE utf8mb4_general_ci;
USE ejercicio_01;

CREATE TABLE cliente (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nif VARCHAR(15) NOT NULL UNIQUE,
    nombre VARCHAR(55) NOT NULL,
    ciudad VARCHAR(15) NOT NULL,
    telefono VARCHAR(25) NOT NULL
);

CREATE TABLE coche (
    matricula VARCHAR(15) UNIQUE PRIMARY KEY,
    marca VARCHAR(15) NOT NULL,
    modelo VARCHAR(15) NOT NULL,
    color VARCHAR(15) NOT NULL,
    pvp DECIMAL(5 , 2 ) NOT NULL,
    cod_cliente INT UNSIGNED NOT NULL,
    FOREIGN KEY (cod_cliente)
        REFERENCES cliente (codigo)
);

CREATE TABLE revisiones (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    tipo_mantenimiento VARCHAR(100) NOT NULL,
    matricula_coche VARCHAR(15) NOT NULL,
    FOREIGN KEY (matricula_coche)
        REFERENCES coche (matricula)
);
