DROP DATABASE IF EXISTS ejercicio_07;
CREATE DATABASE ejercicio_07;
USE ejercicio_07;


CREATE TABLE viajeros (
    dni VARCHAR(25) PRIMARY KEY,
    nombre VARCHAR(55) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono VARCHAR(25) NOT NULL
);

CREATE TABLE lugares (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE viajes (
    codigo VARCHAR(15) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    otros_datos VARCHAR(255) NOT NULL,
    plazas INT UNSIGNED,
    fecha DATE,
    viajero_contrata VARCHAR(25) NOT NULL,
    origen INT UNSIGNED,
    destino INT UNSIGNED,
    FOREIGN KEY (viajero_contrata)
        REFERENCES viajeros (dni),
    FOREIGN KEY (origen)
        REFERENCES lugares (id),
    FOREIGN KEY (destino)
        REFERENCES lugares (id)
);