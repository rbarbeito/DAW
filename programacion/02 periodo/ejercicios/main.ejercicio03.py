margen_izquierdo = 4
titulo = 0
lista_num = []

opciones_menu = ["CALCULADORA", "MENÚ",
                 "1. Sumar",
                 "2. Restar",
                 "3. Dividir",
                 "4. Multiplicar",
                 "5. Resto",
                 "6. Raíz Cuadrada",
                 "0. Salir"]


x_menu = -1
while x_menu != 0:

    for m in range(len(opciones_menu)):
        if titulo < len(opciones_menu[m]):
            titulo = len(opciones_menu[m])

    long = titulo + margen_izquierdo * 2
    # medio_long=lon//2
    long_titulo = (long-len(opciones_menu[0]))//2
    long_titulo_menu = (long-len(opciones_menu[1]))//2

    print()
    print("*"*long)
    print(" "*long_titulo + opciones_menu[0])
    print(" "*long_titulo_menu + opciones_menu[1])
    print("*"*long)
    for m in range(2, len(opciones_menu)):
        print(" "*margen_izquierdo + opciones_menu[m])
    print("*"*long)

    x_menu = int(input("Seleccione la operación: "))

    operation = True
    resultado = 0

    if x_menu == 1:

        while operation:
            operation = False
            num = input("Número a sumar, ('R' para resultado): ")

            print(type(num))

            if num != "r" and num != "R":
                resultado += int(num)
                operation = True

        print("La suma de tus números es:", resultado)

    if x_menu == 2:

        while operation:
            operation = False
            num = input("Número a sumar, ('R' para resultado): ")

            print(type(num))

            if num != "r" and num != "R":
                resultado += int(num)
                operation = True

        print("La suma de tus números es:", resultado)
