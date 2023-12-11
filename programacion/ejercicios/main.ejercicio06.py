import random

errores_permitidos = 7
margen_izquierdo = 4
titulo = 0
categoria = ""
palabra = ""

opciones_menu = ["JUEGO DEL AHORCADO", "MENÚ", "1. Reglas",
                 "2. Escoger categoria", "3. Iniciar Juego", "0. Salir"]


tematicas_list = ['frutas', 'animales', 'paises', 'colores',
                  "Tecnología", "Deportes", "Comida", "Música"]
frutas_list = ["Manzana", "Platano", "Fresa", "Uva", "Pera"]
animales_list = ["Perro", "Gato", "Elefante", "Tigre", "Delfin"]
paises_list = ["Chile", "Francia", "Grecia", "Egipto", "Cuba"]
colores_list = ["Rojo", "Verde", "Azul", "Amarillo", "Blanco"]
tecno_list = ["Robot", "Internet", "Bluetooth", "Hardware", "Software"]
deportes_list = ["Tenis", "Baloncesto", "Ciclismo", "Voleibol", "Boxeo"]
comida_list = ["Sushi", "Pizza", "Pasta", "Hamburguesa", "Tacos"]
musica_list = ["Rock", "Pop", "Jazz", "Blues", "Reggae"]


AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']


x_menu = -1
while x_menu != 0:

    for m in range(len(opciones_menu)):
        if titulo < len(opciones_menu[m]):
            titulo = len(opciones_menu[m])

    long = titulo + margen_izquierdo * 2
    # medio_long=lon//2
    long_titulo = (long-len(opciones_menu[0]))//2

    print("\n")
    print("*"*long)
    print(" "*long_titulo + opciones_menu[0])
    print("*"*long)
    for m in range(1, len(opciones_menu)):
        print(" "*margen_izquierdo + opciones_menu[m])
    print("*"*long)

    x_menu = int(input("Seleccione una opción: "))

    print()

    if x_menu == 1:
        print("REGLAS")
        print()
        print("1. El jugador debe seleccionar una categoria donde jugar")
        print("2. El jugador tiene un total de",
              errores_permitidos,  "posibles fallos para no perder")
        print("3. La palabra que se va adivinar, sera escogida al azar por la computadora, de la categoria seleccionada")

    elif x_menu == 2:
        print("ESCOGER CATEGORIA")
        print()
        for i in range(len(tematicas_list)):
            print(str(i+1)+". "+tematicas_list[i])

        print()
        categoria = int(input("Seleccione una categoria: "))
        if categoria > 8:
            print("Su elección no se encuentra en las opciones.  (-_-;)")
            continue

    elif x_menu == 3:

        if categoria == "":
            print("Debe seleccionar una categoria antes de comenzar el juego")
            continue
        elif categoria == 1:
            palabra = frutas_list[random.randint(1, len(frutas_list))-1]
        elif categoria == 2:
            palabra = animales_list[random.randint(1, len(animales_list))-1]
        elif categoria == 3:
            palabra = paises_list[random.randint(1, len(paises_list))-1]
        elif categoria == 4:
            palabra = colores_list[random.randint(1, len(colores_list))-1]
        elif categoria == 5:
            palabra = tecno_list[random.randint(1, len(tecno_list))-1]
        elif categoria == 6:
            palabra = deportes_list[random.randint(1, len(deportes_list))-1]
        elif categoria == 7:
            palabra = comida_list[random.randint(1, len(comida_list))-1]
        elif categoria == 8:
            palabra = musica_list[random.randint(1, len(musica_list))-1]
        else:
            print("La categoria que seleccionó, no se encuentra en las opciones.  (-_-;)")
            continue

        print("COMENZAMOS EL JUEGO")
        print()
        print("- "*len(palabra))

        lista_palabra = []
        lista_palabra_vacia = []

        for i in palabra:
            lista_palabra.append(i)
            lista_palabra_vacia.append("_")

        contador_errores = 0
        letras_descubiertas = 0

        while contador_errores < errores_permitidos:
            print()
            letra = input("Teclee su opción: ")

            cuenta_rayas = 0
            comprobador = 0

            for x in range(len(lista_palabra_vacia)):
                if lista_palabra_vacia[x] == "_":
                    cuenta_rayas += 1

            for x in range(len(lista_palabra)):

                if letra.upper() == lista_palabra[x].upper():
                    lista_palabra_vacia[x] = letra
                else:
                    if lista_palabra_vacia[x] == "_":
                        comprobador += 1

            if comprobador == cuenta_rayas:
                print(AHORCADO[contador_errores])
                contador_errores += 1

                if errores_permitidos-contador_errores == 1:
                    intento = "intento"
                elif errores_permitidos-contador_errores == 0:
                    print("Perdiste todas tus oportunidades, Intenta nuevamente.")
                    print("La palabra oculta era:", palabra.upper())
                    break
                else:
                    intento = "intentos"

                print("Te quedan " + str(errores_permitidos -
                                         contador_errores) + " " + intento)
            else:
                cuenta_rayas = 0
                for x in range(len(lista_palabra_vacia)):
                    if lista_palabra_vacia[x] == "_":
                        cuenta_rayas += 1

                if cuenta_rayas == 0:
                    print("¡FELICIDADES, ADIVINASTE LA PALABRA  (*_*)")
                    print("La palabra oculta era:", palabra.upper())
                    break

            print("\n")
            for j in range(len(lista_palabra_vacia)):
                print(lista_palabra_vacia[j].upper(), " ", end="")

            print("\n")
