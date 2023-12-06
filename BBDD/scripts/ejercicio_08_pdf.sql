DROP DATABASE IF EXISTS ejercicio_08;
CREATE DATABASE ejercicio_08;
USE ejercicio_08;

CREATE TABLE cliente (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    telefono VARCHAR(25),
    domicilio VARCHAR(100),
    razon_social VARCHAR(100)
);

CREATE TABLE proyectos (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL,
    cuantia DECIMAL(8 , 2 ) NOT NULL,
    inicio DATE NOT NULL,
    fin DATE NOT NULL,
    cliente INT UNSIGNED,
    FOREIGN KEY (cliente)
        REFERENCES proyectos (codigo)
);

CREATE TABLE tipos_pagos (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(50)
);


CREATE TABLE pagos (
    numero INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    concepto VARCHAR(150) NOT NULL,
    cantidad DECIMAL(8 , 2 ) NOT NULL,
    fecha DATE NOT NULL,
    tipo_pago INT UNSIGNED,
    FOREIGN KEY (tipo_pago)
        REFERENCES tipos_pagos (codigo)
);

CREATE TABLE colaboradores (
    nif VARCHAR(15) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    domicilio VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    banco VARCHAR(20) NOT NULL,
    no_cuenta VARCHAR(40) NOT NULL
);

CREATE TABLE coloaboradores_reciben_pagos (
    nif_colaborador VARCHAR(15) NOT NULL,
    numero_pago INT UNSIGNED,
    FOREIGN KEY (nif_colaborador)
        REFERENCES colaboradores (nif),
    FOREIGN KEY (numero_pago)
        REFERENCES pagos (numero)
);

CREATE TABLE colaboradores_participan_proyectos (
    nif_colaborador VARCHAR(15) NOT NULL,
    codigo_proyecto INT UNSIGNED,
    FOREIGN KEY (nif_colaborador)
        REFERENCES colaboradores (nif),
    FOREIGN KEY (codigo_proyecto)
        REFERENCES proyectos (codigo)
);




