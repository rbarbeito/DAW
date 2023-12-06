DROP DATABASE IF EXISTS ejercicio_09;
CREATE DATABASE ejercicio_09;
USE ejercicio_09;

CREATE TABLE profesores (
    dni VARCHAR(15) PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    apellidos VARCHAR(45) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    problacion VARCHAR(25) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    codigo_postal VARCHAR(10) NOT NULL,
    telefono VARCHAR(25) NOT NULL,
    categoria SET('Tutor', 'No Tutor')
);

CREATE TABLE cursos (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    dni_profesor VARCHAR(15) NOT NULL    
);

CREATE TABLE aulas (
    codigo varchar(10) PRIMARY KEY,
    piso INT UNSIGNED NOT NULL,
    no_pupitres INT UNSIGNED NOT NULL
);

CREATE TABLE alumnos (
    dni VARCHAR(15) PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    apellidos VARCHAR(45) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    poblacion VARCHAR(15) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    codigo_postal VARCHAR(10) NOT NULL,
    telefono VARCHAR(15) NOT NULL
);

CREATE TABLE asignaturas (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    horas DECIMAL(2 , 2 ) NOT NULL,
    codigo_curso INT UNSIGNED NOT NULL,
    dni_profesor VARCHAR(15) NOT NULL,
    FOREIGN KEY (codigo_curso)
        REFERENCES cursos (codigo),
    FOREIGN KEY (dni_profesor)
        REFERENCES profesores (dni)
);

CREATE TABLE alumno_matricula_asignatura (
    dni_alumno VARCHAR(15) NOT NULL,
    codigo_asignatura INT UNSIGNED NOT NULL,
    incidencias VARCHAR(255),
    notas DECIMAL(3 , 2 ) NOT NULL,
    FOREIGN KEY (dni_alumno)
        REFERENCES alumnos (dni),
    FOREIGN KEY (codigo_asignatura)
        REFERENCES asignaturas (codigo)
);

CREATE TABLE asignatura_imparte_aula (
    codigo_asignatura INT UNSIGNED NOT NULL,
    codigo_aula VARCHAR(10) NOT NULL,
    dia VARCHAR(2) NOT NULL,
    mes VARCHAR(2) NOT NULL,
    hora TIME NOT NULL,
    FOREIGN KEY (codigo_asignatura)
        REFERENCES asignaturas (codigo),
    FOREIGN KEY (codigo_aula)
        REFERENCES aulas (codigo)
);









