DROP DATABASE if EXISTS ejercicio_05;
CREATE DATABASE ejercicio_05 CHARSET utf8mb4 COLLATE utf8mb4_general_ci;
USE ejercicio_05;

CREATE TABLE guerra (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    inicio DATETIME NOT NULL,
    fin DATETIME NOT NULL
);

CREATE TABLE paises (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    unicio_indep DATETIME NOT NULL,
    fin_indep DATETIME NOT NULL,
    pais_exist BOOLEAN NOT NULL,
    bando ENUM('aliado', 'enemigo')
);

CREATE TABLE paises_intervienen_guerra (
    codigo_guerra INT UNSIGNED NOT NULL,
    codigo_paises INT UNSIGNED NOT NULL,
    incorporan DATETIME NOT NULL,
    retiran DATETIME NOT NULL,
    ganador INT UNSIGNED NOT NULL,
    FOREIGN KEY (codigo_guerra)
        REFERENCES guerra (codigo),
    FOREIGN KEY (codigo_paises)
        REFERENCES paises (codigo),
    FOREIGN KEY (ganador)
        REFERENCES paises (codigo)
);