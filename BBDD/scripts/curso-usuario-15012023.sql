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
    asigantura VARCHAR(50),
    capacidad SMALLINT UNSIGNED,
    idusuario INT UNSIGNED,
    FOREIGN KEY (idusuario)
        REFERENCES usuarios (idusuario) ON UPDATE CASCADE
);