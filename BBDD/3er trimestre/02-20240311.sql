use tienda_v;

select empresa, poblacion from clientes;

select nombre_articulo from productos where seccion='ceramica';

select nombre_articulo, precio from productos where seccion = 'deportes' and precio between 100 and 200;

select nombre_articulo from productos where pais_origen != 'españa';


select nombre_articulo, seccion,pais_origen, precio from productos where seccion ='deportes' and pais_origen='españa' or precio > 350;


select nombre_articulo, seccion, fecha from productos ;