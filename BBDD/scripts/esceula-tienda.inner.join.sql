-- use tienda_2024;
-- inner join
-- Realiza una interseccion entre ambas tablas

-- SQL 1  - metodo antiguo, menos eficiente y realiza el producto cartesiano 
-- select * from clientes C, pedidos P
-- where C.codigo_cliente= P.codigo_cliente;


-- SQL 2
-- select * from clientes C inner join pedidos P
-- ON C.codigo_cliente=P.codigo_cliente


USE escuela;

-- Obtener todos los profesosres los cursos que imparten
select * from curso C inner join profesor P
on C.id_profesor = P.id_profesor;


-- Obtenert todos los cursos en los que esta matriuclado el alumno con id 1
select C.titulo from curso C
inner join alumno_curso AC
on AC.id_curso  = C.id_curso
where AC.id_alumno ='1';

-- Obtener todos los cursos donde esta matriuclado el alumno pablo hernandez;
SELECT   alumno.nombre,   alumno.apellido,   curso.titulo
FROM alumno_curso AC
Inner JOIN alumno
  ON alumno.id_alumno = AC.id_alumno
Inner JOIN curso
  ON curso.id_curso = AC.id_curso
  ORDER BY curso.titulo, alumno.nombre, alumno.apellido;
