DROP DATABASE IF EXISTS tienda_pieza;
CREATE DATABASE tienda_pieza CHARSET utf8mb4 COLLATE utf8mb4_general_ci;
USE tienda_pieza;

CREATE TABLE categoria (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE pieza (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    color VARCHAR(25) NOT NULL,
    precio DECIMAL(7 , 2 ),
    -- precio FLOAT(7 , 2 ),
    -- precio DOUBLE(7 , 2 ),
    codigo_categoria INT UNSIGNED NOT NULL,
    FOREIGN KEY (codigo_categoria)
        REFERENCES categoria (codigo)
);

CREATE TABLE proveedor (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(150) not null,
    ciudad VARCHAR(50) not null,
    provincia VARCHAR(50) not null
);

CREATE TABLE proveedor_suministra_pieza (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    codigo_proveedor INT UNSIGNED,
    codigo_pieza INT UNSIGNED,
    fecha DATE NOT NULL,
    cantidad INT UNSIGNED NOT NULL,
    FOREIGN KEY (codigo_proveedor) REFERENCES proveedor(codigo),
    FOREIGN KEY (codigo_pieza) REFERENCES pieza(codigo)
);



