DROP DATABASE IF EXISTS ejercicio_03;
CREATE DATABASE ejercicio_03 CHARSET utf8mb4 COLLATE utf8mb4_general_ci;
USE ejercicio_03;

CREATE TABLE cliente (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    apellidos VARCHAR(45) NOT NULL,
    direccion VARCHAR(150) NOT NULL,
    telefono VARCHAR(25) NOT NULL
);

CREATE TABLE producto(
codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
descripcion VARCHAR(200) NOT NULL,
precio DECIMAL(5,2) NOT NULL,
existencia INT UNSIGNED NOT NULL DEFAULT(0)
);

CREATE TABLE proveedor (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellidos VARCHAR(45) NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    provincia VARCHAR(15) NOT NULL,
    telefono VARCHAR(25) NOT NULL
);

CREATE TABLE proveedor_suministra_producto (
    codigo_proveedor INT UNSIGNED,
    codigo_producto INT UNSIGNED,
    FOREIGN KEY (codigo_proveedor)
        REFERENCES proveedor (codigo),
    FOREIGN KEY (codigo_producto)
        REFERENCES producto (codigo)
);

CREATE TABLE cliente_compra_producto(
codigo_cliente INT UNSIGNED,
codigo_producto INT UNSIGNED,
fecha DATETIME DEFAULT(current_timestamp()),
FOREIGN KEY(codigo_cliente) references cliente(codigo),
FOREIGN KEY(codigo_producto) REFERENCES producto(codigo)
);