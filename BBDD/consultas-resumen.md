# Consultas resumen

```SQL

select

from

where

group by

having

order by

limit
```

## Funciones de agregación

 > Solo se puede usar en el `SELECT` y en el `HAVING`

 ```sql
 -- COUNT(*) --numero de filas del resultado de la consulta incluyendo los nulos

 select count(*) from alumnos
 >> 10

 -- COUNT(columna) --numero de valores **no nulos** que tiene el resultado de la consulta

 select count(teléfono) from alumno;
 >> 5


 select count(distinct region) from company.offices; --Cuenta las regiones distintas en la tabla `offices` de la base de datos `company`

 ```

