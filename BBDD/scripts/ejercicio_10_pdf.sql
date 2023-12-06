DROP DATABASE IF EXISTS ejercicio_10;
CREATE DATABASE ejercicio_10;
USE ejercicio_10;


CREATE TABLE posicion (
    id_posicion INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    posicion VARCHAR(25) NOT NULL
);

CREATE TABLE equipos (
    codigo VARCHAR(15) PRIMARY KEY,
    fundacion DATE NOT NULL,
    ciudad VARCHAR(20) NOT NULL
);

CREATE TABLE jugadores (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE,
    posicion INT UNSIGNED,
    equipo VARCHAR(15),
    FOREIGN KEY (posicion)
        REFERENCES posicion (id_posicion),
    FOREIGN KEY (equipo)
        REFERENCES equipos (codigo)
);

CREATE TABLE presidentes (
    dni VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    apellidos VARCHAR(45) NOT NULL,
    fecha_nacimiento DATE NOT NULL
);

CREATE TABLE partidos (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    goles_casa INT UNSIGNED NOT NULL DEFAULT 0,
    goles_visitador INT UNSIGNED NOT NULL DEFAULT 0,
    fecha DATE NOT NULL
);

CREATE TABLE estadios (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    aforo INT UNSIGNED
);

CREATE TABLE goles (
    identificador INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    minuto INT UNSIGNED NOT NULL,
    descripcion VARCHAR(200) NOT NULL,
    codigo_partido INT UNSIGNED NOT NULL,
    FOREIGN KEY (codigo_partido)
        REFERENCES partidos (codigo)
);

CREATE TABLE equipo_juega_partido_en_estadio (
    codigo_equipo VARCHAR(15) NOT NULL,
    id_estadio INT UNSIGNED NOT NULL,
    codigo_partido INT UNSIGNED NOT NULL,
    FOREIGN KEY (codigo_equipo)
        REFERENCES equipos (codigo),
    FOREIGN KEY (id_estadio)
        REFERENCES estadios (id),
    FOREIGN KEY (codigo_partido)
        REFERENCES partidos (codigo)
);

ALTER TABLE equipos 
add COLUMN presidente VARCHAR(20) after ciudad,
add CONSTRAINT fk_pres FOREIGN KEY(presidente) REFERENCES presidentes(dni);

ALTER table presidentes
add column equipo varchar(15) after fecha_nacimiento,
add CONSTRAINT fk_equi FOREIGN KEy(equipo) REFERENCES equipos(codigo);




