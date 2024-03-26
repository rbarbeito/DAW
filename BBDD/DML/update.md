## UPDATE and DELETE

> Siempre hay que acordarse de la clausula  `WHERE` ya que se cambiarían todos los registros de la base de datos

### UPDATE
```sql
-- Actualizando por el id del usuario
Update usuario 
set  edad= 18
where id=1;
```

```sql
UPDATE usuario
SET  edad=18
WHERE email="pepe@pepe.com"
```

### DELETE
```sql
Delete from usuarios
where edad > 50;
```