# REDES

Nodo: Cada maquina o computadora es un nodo

- Teoria de redes o grafos(buscar)
- Historia de puentes de `KONIGSBERG`

> Si todos los nodos tienen conexiones impar es imposible recorrer todos los lugares sin pasar aunque sea una sola vez por uno de los puntos

> Tiene que tener maximo 2 nodos impares para tener solución.

## Teoría de Grafos

En matemáticas y en ciencias de la computación, la teoría de grafos (también llamada teoría de las gráficas) estudia las propiedades de los grafos (también llamadas gráficas). Un grafo es un conjunto, no vacío, de objetos llamados vértices (o nodos) y una selección de pares de vértices, llamados aristas (edges en inglés) que pueden ser orientados o no. Típicamente, un grafo se representa mediante una serie de puntos (los vértices) conectados por líneas (las aristas).

### Tipos

`Grafo conexo:` todos los nodos estan conectados por al menos 1 camino

`Grafo no conexo:` No todos los nodos estan conectado por al menos 1 camino, dando como resultado 2 grafos diferentes

`Ciclo: ` Cuando un camino se cierra y vuelve al punto inicial

`Completo:` Todos vertices estan conectados por una arista con todos los nodos

`Hamilteniano:` Se recorre completo sin pasar 2 veces por el mismo nodo

`Ciclo Hamiltoniano`: Se inicia y termina en mismo nodo, y pasa por todos los nodos una sola vez

`Ciclo euleriano:`

`arbol:`

### Tipos de nodos

`Fuentes`: De donde solo salen los caminos

`Destino`: A donde solo llegan los caminos

`Fuentes-Destinos`: En este nodo llegan y salen caminos

## Algoritmo de PRIM

El algoritmo de `Prim` permite encontrar un árbol recubridor mínimo de un grafo. En otras palabras, el algoritmo encuentra un subconjunto de aristas que forman un árbol con todos los vértices, donde el peso total de todas las aristas en el árbol es el mínimo posible.

### Reglas
1. Se busca la arista de menor peso.
2. Se puede usar cualquier arista siempre y cuando ya este conectada a un nodo utilizado.
3. No se pueden crear ciclos.


## Clasificación de las redes

- Redes punto a punto
- Redes entre iguales
- Redes basadas en servidores centrales

### Cliente-servidor

- Servidores de correo
- Servidores de impresion
- World Wide Web

`Cliente:` Demandante de servicios

`Servidores:` Proveedores de servicios. Puede ser tambien un ordenador que comparte sus perifericos con otros ordenadores.

`Definicion 1:` Programas de computadoras en ejecución que atienden las peticiones de otros programas. 

`Definicion2:` Tipo de software que realiza ciertas tareas en nombre de los usuarios. 

