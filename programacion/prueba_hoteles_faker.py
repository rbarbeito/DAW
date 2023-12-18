# Desde el cmd ejecutar: pip install Faker

from faker import Faker
from random import choices, randint

fake = Faker()


# El [6,8] es la probabilidad de salir el primer argumento o el segundo.
# Podeis jugar con ellos pra simular distintas temporadas del año. Más ocupación o menos
# Por ejemplo si poneis [1,0] estará todo lleno. Ya que la probabilidad de que salga el '-' es cero.
# Jugar con diferentes valores para probar.

# negocio = [[["".join(choices([fake.name(), '-'], [1,0])) for _ in range(40)] for _ in range(15)] for _ in range(3)]


# negocio = [[["".join(choices([fake.name(), '-'], [1,0])) for _ in range(40)] for _ in range(15)] for _ in range(3)]

# for i in negocio:
#     print(i)

# print(negocio)

# print("".join(
#     choices(fake.name(), '-', [1,0])
#     ))

# ocupadas = 0
# libres = 0
# for hotel in negocio:
#     for planta in hotel:
#         for habitacion in planta:
#             if habitacion != '-':
#                 ocupadas += 1
#             else:
#                 libres += 1

# print("Habitaciones ocupadas:", ocupadas)
# print("Habitaciones libres:", libres)

# EJERCICIOS PROPUESTOS

# Programa gestion de hoteles. Basica
# ------------------------------------------
# Nivel de habitaciones ocupadas y libres en el negocio. (Dada ya por el profesor)
##
# A realizar por el alumno
# -------------------------------------------
# Calcular las ganancias totales. (Imaginamos un valor por habitacion)
# Desglose de ganancias por hoteles.
# Todo lo anterior pero dependiendo la habitación y/o hotel y/o planta vale mas o menos dinero.
# Saber que plantas son las más demandadas.
# Listado de las X habitaciones favoritas y las menos demandadas.
# Aplicar un descuento a los primeros 30 clientes de cada hotel.
# Debe salir en el precio total con el desglose de los descuentos y en que habitaciones o nombres se dio.
# Hacer registro de gente pero como si ciertas plantas y/o habitaciones, no pueden reservarse por X motivos.
# Simular distintas temporadas dependiendo de donde están los hoteles y calcular los ejercicios anteriores.
# Se trata de hacer o intentar que se parezca lo más posible a una aplicación real.
# Toda mejora o implementacion extra sera bienvenida.
# Darle vida de forma aleatoria que durante X tiempo clientes vayan y vengan e interactuen con la app.
# Modo SIMS durante X tiempo que vaya solo y al final nos de como las stats del dia.


margen_izquierdo = 4
titulo = 0
lista_num = []

opciones_menu = ["HOTEL \"El ENCANTO\"", "MENÚ",
                 "1. Defina la temporada",
                 "2. Ganancias totales de la temporada",
                 "3. Desglose de ganancias por hoteles",
                 "4. Habitación y/o hotel y/o planta vale mas o menos dinero",
                 "5. Saber que plantas son las más demandadas",
                 "0. Salir"]

temporadas = ["MENÚ TEMPORADAS", "1. Primavera",
              "2. Verano", "3. Otoño", "4. Invierno"]

opciones_ocupacion = [[1, randint(0, 10)] for _ in range(4)]
precios = [45, 70, 100]
precios_diferenciados = [
    [[randint(45, 100) for _ in range(40)] for _ in range(15)] for _ in range(3)]

negocio = []
negocio_year = []

menu = -1
while menu != 0:

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

    menu = int(input("Seleccione su opción: "))

    print()

    if menu == 1:
        for m in range(len(temporadas)):
            if titulo < len(temporadas[m]):
                titulo = len(temporadas[m])

        long = titulo + margen_izquierdo * 2
        long_titulo = (long-len(temporadas[0]))//2
        long_titulo_menu = (long-len(temporadas[1]))//2

        print()
        print("*"*long)
        print(" "*long_titulo + temporadas[0])
        print("*"*long)
        for m in range(1, len(temporadas)):
            print(" "*margen_izquierdo + temporadas[m])
        print("*"*long)

        menu_temporada = int(input("Seleccione su temporada: "))

        temporada_seleccionada = temporadas[menu_temporada][3:]

        print(temporada_seleccionada)
        print("opciones_ocupacion", opciones_ocupacion)

        for i in range(4):
            negocio = [[["".join(choices([fake.name(), '-'], opciones_ocupacion[i]))
                         for _ in range(40)] for _ in range(15)] for _ in range(3)]
            negocio_year.append(negocio)

    elif menu == 2:
        acumulado_normal = acumulado_medium = acumulado_premiun = 0

        for hotel in negocio:
            for planta in hotel:
                for i in range(len(planta)):
                    if i >= 0 and i < 5 and planta[i] != "-":
                        acumulado_normal += precios[0]
                    elif i >= 5 and i < 11 and planta[i] != "-":
                        acumulado_medium += precios[1]
                    elif i >= 12 and planta[i] != "-":
                        acumulado_premiun += precios[2]

        print("Los ingresos en la tempoada de", temporada_seleccionada,
              "en las habitaciones normales fue de:", acumulado_normal)
        print("Los ingresos en la tempoada de", temporada_seleccionada,
              "en las habitaciones medium fue de:", acumulado_medium)
        print("Los ingresos en la tempoada de", temporada_seleccionada,
              "en las habitaciones premium fue de:", acumulado_premiun)
        print("Los ingresos totales de la temporada", temporada_seleccionada,
              "fueron de", acumulado_normal+acumulado_medium+acumulado_premiun)

    elif menu == 3:
        acumulado_normal = acumulado_medium = acumulado_premiun = 0
        ganancia_por_hoteles = []

        for hotel in negocio:
            for planta in hotel:
                for i in range(len(planta)):
                    if i >= 0 and i < 5 and planta[i] != "-":
                        acumulado_normal += precios[0]
                    elif i >= 5 and i < 11 and planta[i] != "-":
                        acumulado_medium += precios[1]
                    elif i >= 12 and planta[i] != "-":
                        acumulado_premiun += precios[2]

                ganancia_por_hoteles.append(
                    acumulado_normal+acumulado_medium+acumulado_premiun)

        print("Las ganancias en la temporada de",
              temporada_seleccionada, " por hoteles")
        print("Hotel 1:", ganancia_por_hoteles[0])
        print("Hotel 2:", ganancia_por_hoteles[1])
        print("Hotel 3:", ganancia_por_hoteles[2])

    elif menu == 4:
        acumulado = [[0 for _ in range(3)] for _ in range(3)]

        for hotel in range(len(negocio)):
            for planta in range(len(negocio[hotel])):
                for habt in range(len(negocio[hotel][planta])):
                    if habt == 1 and planta == 1:
                        print(hotel, planta, habt,
                              precios_diferenciados[hotel][planta][habt])

                    if habt >= 0 and habt < 5 and negocio[hotel][planta][habt] != "-":
                        acumulado[hotel][0] += precios_diferenciados[hotel][planta][habt]
                    elif habt >= 5 and habt < 12 and negocio[hotel][planta][habt] != "-":
                        acumulado[hotel][1] += precios_diferenciados[hotel][planta][habt]
                    elif habt >= 12 and negocio[hotel][planta][habt] != "-":
                        acumulado[hotel][2] += precios_diferenciados[hotel][planta][habt]

        print(acumulado)

        print("Las ganancias en la temporada de",
              temporada_seleccionada, " por hoteles")
        print("Hotel 1:", acumulado[0][0]+acumulado[0][1]+acumulado[0][2])
        print("Hotel 2:", acumulado[1][0]+acumulado[1][1]+acumulado[1][2])
        print("Hotel 3:", acumulado[2][0]+acumulado[2][1]+acumulado[2][2])
        print()
        print("Ganancia en las habitaciones normales", acumulado[0][0]+acumulado[1][0]+acumulado[2][0])
        print("Ganancia en las habitaciones normales", acumulado[0][1]+acumulado[1][1]+acumulado[2][1])
        print("Ganancia en las habitaciones normales", acumulado[0][2]+acumulado[1][2]+acumulado[2][2])

    elif menu==5:
        print()