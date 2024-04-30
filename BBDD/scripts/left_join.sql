use tienda_2024;
select * from clientes C left join pedidos P
On C.codigo_cliente = P.codigo_cliente;