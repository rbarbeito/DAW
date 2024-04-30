use tienda_2024;

select * from productos where seccion='deportes'
union
select * from productosnuevos where seccion = 'deportes de riesgo'; 


-- Queremos conocer los articulos de precio mayor de 500 euros y de la seccion de alta costura
select * from productos where precio > 500
union
select * from productosnuevos where seccion="alta costura";


-- no value repetidos
select * from productos
where seccion='deportes'
union all
select * from productosnuevos;
