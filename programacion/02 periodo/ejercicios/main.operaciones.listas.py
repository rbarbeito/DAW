lista = [1, 3, 4, 5, 6, 7, 82]
rango = range(len(lista))

print("Teniendo en cuenta la lista:", lista,
      "Defina la accion a realizar con sus elementos\n")
accion = "5"

while accion != "0":
    print("Menú\n", "1. Sumar\n", "2. Restar\n", "3. Multiplicar\n",
          "4. Exponenciar\n", "0. Salir", sep="")
    accion = input("Escoja la accion a realizar: ")

    if accion == "1":
        numero = int(
            input("Que numero deseas sumar a cada elemento de la lista:"))
        for i in rango:
            lista[i] = lista[i]+numero

        print("Su nueva lista ahora tiene estos valores:", lista)
    elif accion == "2":
        numero = int(
            input("Que numero deseas restar a cada elemento de la lista:"))
        for i in rango:
            lista[i] = lista[i]-numero

        print("Su nueva lista ahora tiene estos valores:", lista)
    elif accion == "3":
        numero = int(
            input("Que numero deseas multiplicar a cada elemento de la lista:"))
        for i in rango:
            lista[i] = lista[i]*numero

        print("Su nueva lista ahora tiene estos valores:", lista)
    elif accion == "4":
        numero = int(
            input("Que numero deseas exponenciar a cada elemento de la lista:"))
        for i in rango:
            lista[i] = lista[i]**numero

        print("Su nueva lista ahora tiene estos valores:", lista)


print("¡Hasta la vista Baby!")
