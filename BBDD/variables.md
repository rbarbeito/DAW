# Variables globales y variables de sesión

> **Globales** Son persistentes aunque apagues el pc

> **De sesión** Cuando apago la conexión de sesión, las mismas se pierden

```bash
# Mostrar las variables de entorno
SHOW GLOBAL VARIABLES;
SHOW SESSION VARIABLES;

//asi se crea una variable local, esta cambio el formato del tiempo, ha español de España 
set @@SESSION.lc_time_names='es_ES'; 

# Si queremos cambiarla de manera global seria de esta forma:
set @@GLOBAL.lc_time_names='es_ES'

#  Cambiar la zona horaria
SET GLOBAL time_zone='Europe/Madrid'

# Ver la zona horaria de configuracion
SELECT @@GLOBAL.time_zone;

select @@Session.time_zone;

select now();

select curtime(); -- Time actual

select dayname('2007-02-03'); -- Devuelve el dia de semana de esa fecha 
```

# Funciones con select

```SQL
# Funciones Matemáticas
select abs(-25); #- Valor absoluto 

select pi(); #- valor de pi 

select sqrt(9); #- Raíz cuadrada

select round(37.12596,4); #- Redondeo a 4 dígitos

select ceil(4.3); #- Redondeo hacia arriba

select floor(4.3); #- Redondeo hacia abajo

select mod(10,2); #- Modulo de 10

select 1+1 as result; #- Devuelve el valor de 2 en la resouesta

```

# Funciones de controles de flujo

```SQL
-- operador case
use instituto;
select nombre, apellido1, apellido2,
	case es_repetidor
		when 'si' then 'Repite'
                when 'no' then 'No repite'
	end as repite
from alumno;

-- operdador IF
select nombre, apellido1, apellido2,
	if(es_repetidor='si', 'Repite', 'No Repite') as Repite
from alumno;

-- operador ifnull
select nombre, apellido1, apellido2,
	IFNULL(teléfono, 'Teléfono no disponible')
from alumno;

-- operador nullif
select nullif('luis', 'luis9') as nombre; # Compara dos valores si son iguales devuelve null, sino devuelve el primero de los valores

```

# Errores básicos primeras consultas

```SQL
SELECT * FROM alumno WHERE telefono = NULL; #error
SELECT * from alumno WHERE telefono IS NULL; #correcta

select * from alumno where apellido = 'S%' #error
select * from alumno where apellido like 'S%' #correcta

select * from alumno where apellido != 'S%' #error
select * from alumno where apellido not like 'S%' #correcta

select * from alumno where fecha_nacimiento >= '1999/01/01' and '1999/12/31' #error
select * from alumno where fecha_nacimiento >= '1999/01/01' and fecha_nacimiento <= '1999/12/31' #correcta


select 1 + '1'; # suma los valores => 2
select concat(1,'1'); # concatena los numero => 11

```

## Resta de dos valores varchar

```SQL
select '2021-01-31' - '2024-02-01' #error al que querer sacar diferencias entre fechas

```
## Resta de dos valores DATE

```SQL
SELECT CAST('2021-01-31' AS DATE) - cast('2024-02-01' AS DATE) #error al que querer sacar diferencias entre fechas
SELECT DATEDIFF('2021-01-31', '2024-02-01') # Consulta correcta

```

## Usar operadores sumas y restas en fechas


> Los tipos de datos de fecha(`DATE`, `DATETIME`, `TIMESTAMP`) es necesario usar las funciones especificas de mysql


