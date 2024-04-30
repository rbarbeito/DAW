use ropas;

select * from camisas, pantalon;  -- todos los campos

select detalles, description from camisas, pantalon;

select detalles, description, camisas.peso+pantalon.peso from camisas, pantalon; -- calculo del peso de la combinacion adicionando el nombre de la tabla al campo para evitar la ambiguedad


select * from camisas, pantalon , calzado;


Select concat("Camisa de ", C.detalles, ", Pantalon de ", P.description,", Calzado tipo ", Cz.descripcion) as Outfit, C.peso+P.peso+Cz.peso_gr as peso from camisas as C, pantalon as P, calzado as Cz;

select * 
from camisas as C, pantalon as P , calzado as Z
where C.idcamisas = '1';


-- Cuantas mudas se pueden confeccionar con las mudas y los pantalones
 
select count(*) as combinaciones
from camisas as C, pantalon as P ;

select count(*), count(C.detalles), count(distinct C.detalles)
from camisas as C, pantalon as P , calzado as Z;

-- ¿Que mudas o combinaciones son aquellas que la primera camisa se combina con el primer pantalon, la segunda camisa con el segundo pantalon y asi sucesivamente?
select *
from camisas as C, pantalon as P 
where C.idcamisas = P.idpantalon;
