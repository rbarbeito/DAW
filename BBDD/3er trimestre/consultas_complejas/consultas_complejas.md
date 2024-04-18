# Consultas multitablas

1. SQL 86 => SQL1 (Producto cartesiano)
2. SQL 92-2003 => SQL2 (JOINS)



### Productos cartesianos

Es la combinación de todos los elementos de las dos tablas, unos con otros

````sql
use ropas;

-- todos los campos
select * from camisas, pantalon;  

select detalles, description from camisas, pantalon;

-- calculo del peso de la combinacion adicionando el nombre de la tabla al campo para evitar la ambiguedad
select detalles, description, camisas.peso+pantalon.peso from camisas, pantalon; 

```