# Verificar si 3 lados de ciertas longitudes forman un triángulo
# La suma arbitraria de los dos lados tiene que ser mayor que el tercero
# saber si el triangulo es rectángulo c**2 = a**2 + b**
# calcular área de un triangulo s=(a+b+c)/2 ==>> a=sqr(s(s-a)(s-b)(s-c))


def es_triangulo(lista_lados):
    return lista_lados[0] < lista_lados[1] + lista_lados[2] and lista_lados[1] < lista_lados[2]+lista_lados[0] and lista_lados[2] < lista_lados[0]+lista_lados[1]


def es_rectangulo(lista_lados):
    mayor = [lista_lados[0]]
    menores = []
    for i in range(1, len(lista_lados)):
        if mayor[0] < lista_lados[i]:
            menores.append(mayor[0])
            mayor[0] = lista_lados[i]
        else:
            menores.append(lista_lados[i])

    return mayor[0]**2 == menores[0]**+menores[1]**2


def area_rectangulo(lista_lados):
    s = 0
    for n in lista_lados:
        s += n
    s = s/2

    return (s*(s-lista_lados[0])*(s-lista_lados[1])*(s-lista_lados[2]))**0.5


lista_lados = []
print("TRIÁNGULO")

lista_lados.append(int(input("Teclee la longitud del primer lado: ")))
lista_lados.append(int(input("Teclee la longitud del segundo lado: ")))
lista_lados.append(int(input("Teclee la longitud del tercer lado: ")))


print()


if es_triangulo(lista_lados):
    if es_rectangulo(lista_lados):
        print("El triángulo construido es rectángulo")

    print("El área del triángulo es de:", area_rectangulo(lista_lados))
else:
    print("Con esas dimensiones no se puede construir un triángulo")
