use tienda_v;

# 1. Calcular el nombre de los articulos, la seccion y el precio  con el precio mas el 21% de iva añadido
select nombre_articulo, seccion, precio, (precio*1.21) as previoMasIVA
from productos;

# 2. calcular el nombre de los articulos, la seccion y el precio con el precio mas el 21% de iva añadido, añadiendo 2 decimales
select nombre_articulo, seccion, precio, round(precio*1.21,4) as previoMasIVA
from productos;

#3. Un campo nuevo en la consulta anterior que aplique un desuento de 3 euros
select nombre_articulo, seccion, precio, (precio-3) as descuento,  (precio*1.21) as precioMasIVA, ((precio-3) *1.21) as descuentoMasIVA
from productos;

# 4. articulos que muestren los dias de diferencia desde la fecha de introduccion del articulo hasta el dia de hoy
select nombre_articulo, seccion, precio, fecha, NOW() as fecha, datediff(now(), fecha) as diferencia
from productos
where seccion = 'deportes';


select nombre_articulo, seccion, precio, fecha, date_format(NOW(), "%d-%M-%Y") as fecha, datediff(now(), fecha) as diferencia
from productos
where seccion = 'deportes';
