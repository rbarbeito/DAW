drop database if EXISTS pinoteca;
create DATABASE if NOT EXISTS pinoteca;
use pinoteca;

CREATE TABLE pinoteca (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    ciudad VARCHAR(15),
    direccion VARCHAR(100),
    area DECIMAL
);



CREATE TABLE escuelas (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    pais VARCHAR(100),
    fecha_aparicion DATE
);

CREATE TABLE pintor (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    pais VARCHAR(100),
    ciudad VARCHAR(50),
    fecha_nacimiento DATE,
    fecha_defuncion DATE,
    id_escuela INT UNSIGNED,
    maestro INT UNSIGNED,
    FOREIGN KEY (id_escuela)
        REFERENCES escuelas (id),
    FOREIGN KEY (maestro)
        REFERENCES pintor (id)
);

CREATE TABLE cuadros (
    codigo VARCHAR(15) PRIMARY KEY,
    nombre VARCHAR(50),
    dimensiones VARCHAR(50),
    fecha_pintado DATE,
    tecnica VARCHAR(100),
    id_pinoteca INT UNSIGNED,
    id_cuadro int UNSIGNED,
    FOREIGN KEY (id_pinoteca)
        REFERENCES pinoteca (id),
	FOREIGN KEY(id_cuadro) REFERENCES pintor(id)
);


CREATE TABLE mecenas (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    fecha_muerte DATE,
    ciudad_nacmiento VARCHAR(100),
    pais VARCHAR(100),
    fecha DATE
);

CREATE TABLE mecenas_protege_pintor (
    id_pintor INT UNSIGNED,
    id_mecenas INT UNSIGNED,
    FOREIGN KEY (id_pintor)
        REFERENCES pintor (id),
    FOREIGN KEY (id_mecenas)
        REFERENCES mecenas (id)
);