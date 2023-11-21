# Ejercicio 02

![Alt text](image-9.png)

```SQL
SUCURSAL (codigo INT, direccion VARCHAR, telefono INT, ciudad VARCHAR, provincia VARCHAR)

EMPLEADO (id INT, nif VARCHAR, nombre VARCHAR, apellido1 VARCHAR, apellido2 VARCHAR, telefono INT) sucursal_empleado FOREIGN KEY SUCURSAL(codigo)

PERIODISTA(id INT, nombre VARCHAR, apellido1 VARCHAR, apellido2 VARCHAR, telefono INT, especialidad VARCHAR)

REVISTA(numero_registro VARCHAR, titulo VARCHAR, tipo VARCHAR, periodicidad VARCHAR)

SECCION(titulo VARCHAR, extension INT)seccion_revista FOREIGN KEY REVISTA(numero_registro)

EJEMPLAR(fecha DATE, numero_paginas INT, numero_ejemplares INT)ejemplar_revista FOREIGN KEY REVISTA(numero_registro)

REVISTA_PERIODISTA(id INT, revista_codigo INT, periodista_codigo INT)
```