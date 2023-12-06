DROP DATABASE IF EXISTS ejercicio_06;
CREATE DATABASE ejercicio_06 CHARSET utf8mb4 COLLATE utf8mb4_general_ci;
USE ejercicio_06;


CREATE TABLE personas (
    dni VARCHAR(15) PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    apellidos VARCHAR(45) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    poblacion VARCHAR(25) NOT NULL,
    telefono VARCHAR(25) NOT NULL
);

CREATE TABLE vehiculos (
    matricula VARCHAR(25) PRIMARY KEY,
    marca VARCHAR(25) NOT NULL,
    modelo VARCHAR(25) NOT NULL,
    dni_persona VARCHAR(25) NOT NULL,
    FOREIGN KEY (dni_persona)
        REFERENCES personas (dni)
);

CREATE TABLE multas (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    importe DECIMAL(5 , 2 ) NOT NULL,
    lugar VARCHAR(25) NOT NULL,
    hora TIME NOT NULL,
    fecha DATE NOT NULL
);

CREATE TABLE accidentes (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    lugar VARCHAR(25) NOT NULL,
    fecha DATE NOT NULL,
    hora DATE NOT NULL
);

CREATE TABLE personas_vehiculo_aplican_multas (
    dni_persona VARCHAR(25) NOT NULL,
    matricula_vehiculo VARCHAR(25) NOT NULL,
    id_multas INT UNSIGNED,
    FOREIGN KEY (dni_persona)
        REFERENCES personas (dni),
    FOREIGN KEY (matricula_vehiculo)
        REFERENCES vehiculos (matricula),
    FOREIGN KEY (id_multas)
        REFERENCES multas (id)
);

CREATE TABLE personas_vehiculo_intervienen_accidente (
    dni_persona VARCHAR(25) NOT NULL,
    matricula_vehiculo VARCHAR(25) NOT NULL,
    id_accidente INT UNSIGNED,
    FOREIGN KEY (dni_persona)
        REFERENCES personas (dni),
    FOREIGN KEY (matricula_vehiculo)
        REFERENCES vehiculos (matricula),
    FOREIGN KEY (id_accidente)
        REFERENCES accidentes (id)
);