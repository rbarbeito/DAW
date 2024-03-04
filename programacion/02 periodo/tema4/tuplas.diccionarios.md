# Tuplas y diccionarios

> Un **tipo de secuencia es un tipo de dato en Python el cual es capaz de almacenar más de un valor (o ninguno si la secuencia esta vacía), los cuales pueden ser secuencialmente (de ahí el nombre) examinados**, elemento por elemento.

Debido a que el bucle for es una herramienta especialmente diseñada para iterar a través de las secuencias, podemos definirlas de la siguiente manera: **una secuencia es un tipo de dato que puede ser escaneado por el bucle** `for`.

La segunda noción - **la mutabilidad** - es una propiedad de cualquier tipo de dato en Python que describe su disponibilidad para poder cambiar libremente durante la ejecución de un programa. Existen dos tipos de datos en Python: **mutables** e **inmutables.**

## ¿Qué es una tupla?

Lo primero que distingue una lista de una tupla es la sintaxis empleada para crearlas. Las **tuplas utilizan paréntesis,** mientras que las listas usan corchetes, aunque también es **posible crear una tupla tan solo separando los valores por comas**

```Python
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)
```

> (1, 2, 4, 8)
(1.0, 0.5, 0.25, 0.125)

Nota: **cada elemento de una tupla puede ser de distinto tipo** (punto flotante, entero, cadena, o cualquier otro tipo de dato).

### ¿Cómo crear una tupla?

Tupla vacia

```
empty_tuple = ()
```

Tupla de un solo elemento
```
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,
```


Todas estas instrucciones (con excepción de primera) causarán un error de ejecución :

```
my_tuple = (1, 10, 100, 1000)

my_tuple.append(10000)
del my_tuple[0]
my_tuple[1] = -10
```

Este es el mensaje que Python arrojará en la ventana de consola:

> AttributeError: 'tuple' object has no attribute 'append'

### :alien: ¿Qué más pueden hacer las tuplas?

- La función len() acepta tuplas, y regresa el número de elementos contenidos dentro.
- El operador + puede unir tuplas (ya se ha mostrado esto antes).
- El operador * puede multiplicar las tuplas, así como las listas.
- Los operadores in y not in funcionan de la misma manera que en las listas.


Una de las propiedades de las tuplas más útiles es que pueden **aparecer en el lado izquierdo del operador de asignación.** Este fenómeno ya se vio con anterioridad, cuando fue necesario encontrar una manera de intercambiar los valores entre dos variables.

# ¿Qué es un diccionario?

El **diccionario** es otro tipo de estructura de datos de Python. No **es una secuencia** (pero puede adaptarse fácilmente a un procesamiento secuencial) y además es **mutable**.

En el mundo de Python, la palabra que se esta buscando se denomina `clave(key).` La palabra que se obtiene del diccionario es denominada `valor`.

```Python
# Ejemplo
dictionario_telefonos={"jefe": 123456789,"amigo":44679123}
```

La lista de todos los pares es **encerrada con llaves**, mientras que los pares son **separados por comas**, y las **claves y valores por dos puntos**.

El diccionario entero se puede imprimir con una invocación a la función `print()`. 

Primeramente, recordemos que **los diccionarios no son listas** - no guardan el orden de sus datos, el orden no tiene significado (a diferencia de los diccionarios reales). El orden en que un diccionario **almacena sus datos esta fuera de nuestro control**. Esto es normal. (*)


- Si una clave es una cadena, se tiene que especificar como una cadena.
- Las claves son sensibles a las mayúsculas y minúsculas: 'Suzy' sería diferente a 'suzy'.

Ahora algo muy importante: **No se puede utilizar una clave que no exista**.

```Python
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'león', 'caballo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")
```

> gato -> chat
león no está en el diccionario
caballo -> cheval

Cuando escribes una expresión grande o larga, puede ser una buena idea mantenerla alineada verticalmente. Así es como puede hacer que el código sea más legible y más amigable para el programador, por ejemplo:

```Python
# Ejemplo 1:
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
              }

# Ejemplo 2:
phone_numbers = {'jefe': 5551234567,
                 'Suzy': 22657854310
                 }

```

> **Nota:** :sound: Este tipo de formato se llama **sangría francesa**.

## ¿Cómo utilizar un diccionario? 

¿Pueden los diccionarios ser examinados utilizando el bucle for, como las listas o tuplas?

`No,` porque un diccionario no es un tipo de dato secuencial - el bucle for no es útil aquí.

`Si,` porque hay herramientas simples y muy efectivas que pueden adaptar cualquier diccionario a los requerimientos del bucle for (en otras palabras, se construye un enlace intermedio entre el diccionario y una entidad secuencial temporal).

### El método keys()
 ```Python
 dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
```

El código produce la siguiente salida:

> gato -> chat
perro -> chien
caballo -> cheval

### La función sorted()
```Python
for key in sorted(dictionary.keys()):
```
La función sorted() hará su mejor esfuerzo y la salida será la siguiente:

> caballo -> cheval
gato -> chat
perro -> chien

## ¿Cómo utilizar un diccionario? Los métodos item() y values()

### Método items(). 

Este método **regresa una lista de tuplas** (este es el primer ejemplo en el que las tuplas son mas que un ejemplo de si mismas) **donde cada tupla es un par de cada clave con su valor**.

```Python
#Ejemplo

dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "->", french)
```

Salida
>gato -> chat
perro -> chien
caballo -> cheval

### Método values()

Funciona de manera muy similar al de keys(), pero **regresa una lista de valores**.

```Python
#Ejemplo
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for french in dictionary.values():
    print(french)
```


Salida
>chat
chien
cheval

### enumerate()

```Python
#Ejemplo

dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for i,j in dictionary.items():
    print(i,j)
```

salida
>0 chat
1 chien
2 cheval

## ¿Cómo utilizar un diccionario? Modificar, agregar y eliminar valores

El asignar un nuevo valor a una clave existente es sencillo, debido a que los diccionarios son completamente mutables, no existen obstáculos para modificarlos.

Se va a reemplazar el valor "chat" por "minou", lo cual no es muy adecuado, pero funcionará con nuestro ejemplo.

```Python
dictionary = {'gato': 'minou', 'perro': 'chien', 'caballo': 'cheval'}

dictionary['gato'] = 'minou'
print(dictionary)
```

Salida
> {'gato': 'minou', 'dog': 'chien', 'caballo': 'cheval'}

### Agregando nuevas claves

El agregar una nueva clave con su valor a un diccionario es tan simple como cambiar un valor. Solo se tiene que asignar un valor a una nueva **clave que no haya existido antes**.

```Python
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dictionary['cisne'] = 'cygne'
print(dictionary)
```

Salida

> {'gato': 'chat', 'perro': 'chien', 'caballo': 'cheval', 'cisne': 'cygne'}

También es posible insertar un elemento al diccionario utilizando el método `update()`, por ejemplo:

```Python
dictionary.update({"pato": "canard"})
print(dictionary)
```

### Eliminado una clave

Nota: al eliminar la clave también se **removerá el valor asociado. Los valores no pueden existir sin sus claves**.

```Python
#Ejemplo
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

del dictionary['perro']
print(dictionary)
```

> :sound: **Nota:** el eliminar una clave no existente, provocará un error.

Para eliminar el ultimo elemento de la lista, se puede emplear el método `popitem()`:

```Python
#Ejemplo
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dictionary.popitem()
print(dictionary)    # salida: {'gato': 'chat', 'perro': 'chien'}

```

>:sound: **Nota** En versiones anteriores de Python, por ejemplo, antes de la 3.6.7, el método popitem() elimina un elemento al azar del diccionario.