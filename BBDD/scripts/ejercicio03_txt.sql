DROP DATABASE if EXISTS ejercicio01_txt;
CREATE DATABASE ejercicio01_txt CHARSET UTF8MB4 COLLATE UTF8MB4_GENERAL_CI;
USE ejercicio01_txt;


CREATE TABLE sucursales (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    domicilio VARCHAR(100),
    telefono VARCHAR(25)
);

CREATE TABLE empleados (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(25),
    apellidos VARCHAR(45),
    telefono VARCHAR(25),
    id_sucursales INT UNSIGNED,
    FOREIGN KEY (id_sucursales)
        REFERENCES sucursales (codigo)
);

CREATE TABLE revistas (
    registro VARCHAR(100) PRIMARY KEY,
    titulo VARCHAR(100),
    peridicidad VARCHAR(100),
    tipo VARCHAR(10),
    seccion VARCHAR(20)
);

CREATE TABLE periodistas (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nif VARCHAR(20),
    nombre VARCHAR(25),
    apellidos VARCHAR(45),
    telefono VARCHAR(25),
    especialidad VARCHAR(50)
);

CREATE TABLE periodista_escribe_revista (
    registro_revista VARCHAR(100),
    id_periodista INT UNSIGNED,
    FOREIGN KEY (registro_revista)
        REFERENCES revistas (registro),
    FOREIGN KEY (id_periodista)
        REFERENCES periodistas (id)
);

CREATE TABLE ejemplares (
    identificador VARCHAR(100) PRIMARY KEY,
    fecha DATE,
    paginas INT,
    cantidad INT,
    registro_revista VARCHAR(100),
    FOREIGN KEY (registro_revista)
        REFERENCES revistas (registro)
);

CREATE TABLE seccion (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    extension VARCHAR(10)
);

CREATE TABLE revista_tienen_secciones (
    registro_revista VARCHAR(100),
    id_seccion INT UNSIGNED,
    FOREIGN KEY (registro_revista)
        REFERENCES revistas (registro),
    FOREIGN KEY (id_seccion)
        REFERENCES seccion (id)
);


