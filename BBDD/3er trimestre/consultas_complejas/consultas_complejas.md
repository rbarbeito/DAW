# Consultas multitablas

1. SQL 86 => SQL1 (Producto cartesiano)
2. SQL 92-2003 => SQL2 (JOINS)



### Productos cartesianos

Es la combinación de todos los elementos de las dos tablas, unos con otros

```sql
use ropas;

-- todos los campos
select * from camisas, pantalon;  

select detalles, description from camisas, pantalon;

-- cálculo del peso de la combinación adicionando el nombre de la tabla al campo para evitar la ambigüedad
select detalles, description, camisas.peso + pantalon.peso from camisas, pantalon; 

```


> Se aconseja anteponer el nombre de la tabla siempre que se este trabajando con varias tablas en una consulta, para evitar posibles ambigüedades en las consultas.

> Para evitar escribir de mas se utilzan los alias enlas tablas, deben escribirse en mayúsculas

```sql
select C.detalles, P.description, C.peso + P.peso as peso_total from camisas as C, pantalon as P; 
```

## Unión Externa

- UNION
- UNION ALL
- EXCEPT --- **NO MYSQL**
- INTERSECT --- **NO MYSQL**
- MINUS --- **NO MYSQL**


## Unión Interna

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN

