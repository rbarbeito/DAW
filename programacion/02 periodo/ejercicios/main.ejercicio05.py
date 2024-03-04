# 5-)Vamos a crear un programa que tenga el siguiente menú:

# 1-Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
# 2-Añadir número de la lista en una posición: Me pide un número y una posición,
# y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
# 3-Longitud de la lista: te muestra el número de elementos de la lista.
# 4-Eliminar el último número: Muestra el último número de la lista y lo borra.
# 5-Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra
# de ella (la posición se pide a partir de 1).
# 6-Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
# 7-Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
# 8-Mostrar números: Muestra los números de la lista
# 9-Salir

margen_izquierdo = 4
titulo = 0
lista_num = []

opciones_menu = ["TRABAJO CON LISTAS. MENÚ", "1. Añadir número a la lista",
                 "2. Añadir número de la lista en una posición", "3. Longitud de la lista", "4. Eliminar el último número",
                 "5. Eliminar un número", "6. Contar números", "7. Posiciones de un número", "8. Mostrar números", "0. Salir"]


x_menu = -1
while x_menu != 0:

    for m in range(len(opciones_menu)):
        if titulo < len(opciones_menu[m]):
            titulo = len(opciones_menu[m])

    long = titulo + margen_izquierdo * 2
    # medio_long=lon//2
    long_titulo = (long-len(opciones_menu[0]))//2

    print()
    print("*"*long)
    print(" "*long_titulo + opciones_menu[0])
    print("*"*long)
    for m in range(1, len(opciones_menu)):
        print(" "*margen_izquierdo + opciones_menu[m])
    print("*"*long)

    x_menu = int(input("Seleccione la tarea: "))

    print()

    if x_menu == 1:
        num = "A"
        while num != -1:
            num = int(input("Teclee número a guardar, -1 para terminar: "))
            if num == -1:
                break
            lista_num.append(num)

    elif x_menu == 2:
        print("Teniendo esta lista de numeros:", lista_num)

        pos = int(input("En que posición desea insertar el número: "))
        num = int(input("Teclee el número a guardar: "))

        lista_num.insert(pos-1, num)

        print("Su lista ahora tiene estos números:", lista_num)

    elif x_menu == 3:
        print("La longitud de su lista de numeros es:", len(lista_num))

    elif x_menu == 4:

        if len(lista_num) == 0:
            print("Esta operación no se puede reaizar, la lista esta vacía")
        else:
            del lista_num[len(lista_num)-1]
            print("Este es el listado de números en su lista: ", lista_num)

    elif x_menu == 5:

        print("Teniendo en cuenta esta lista:", lista_num)
        num = int(input(
            "Tenga en cuenta que se eliminaran todas las existencias del número en la lista, ¿Cúal número desea eliminar?: "))
        posicion = len(lista_num)-1
        cant = 0
        while posicion >= 0:
            if lista_num[posicion] == num:
                del lista_num[posicion]
                cant += 1
                posicion = len(lista_num)-1
            else:
                posicion -= 1

        if cant > 1:
            print("Se eliminaron", cant, "veces el número", num)
        elif cant == 1:
            print("Se elimino 1 vez el númmero", num)
        else:
            print("El número", num, "no se encontraba en la lista")

        print("Este es el listado de números en su lista: ", lista_num)

    elif x_menu == 6:
        print("Teniendo en cuenta esta lista:", lista_num)
        num = int(input("¿Cúal número desea contar?: "))
        cant = 0
        for i in range(len(lista_num)):
            if lista_num[i] == num:
                cant += 1

        if cant > 1:
            print("Se contó", cant, "veces el número", num)
        elif cant == 1:
            print("Se contó 1 vez el númmero", num)
        else:
            print("El número", num, "no se encontraba en la lista")

    elif x_menu == 7:
        pos = []
        print("Teniendo en cuenta esta lista:", lista_num)
        num = int(input(
            "Se devolveran todas las posiciones donde se encuentre el número. ¿De cúal número desea saber su posición?: "))
        for i in range(len(lista_num)):
            if num == lista_num[i]:
                pos.append[lista_num[i]+1]

        if len(pos) > 1:
            print("El número", num, "se encontro en estas posiciones", pos)
        elif len(pos) == 1:
            print("El número", num, "solo se encontró en la posición", pos[0])
        else:
            print("El número", num, "no se encontraba en la lista")

    elif x_menu == 8:
        print("Este es el listado de números en su lista: ", lista_num)
