# Encontrar la ubicación en una lista de un elemento dado

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ciclo = True
while ciclo:
    ciclo = False
    numero_buscado = int(input("¿Qué número desea buscar?: "))
    if numero_buscado in list:
        for i in range(len(list)):
            if list[i] == numero_buscado:
                print("El numero se encuentra en la posición", i + 1, "de la lista")
    else:
        print("El número", numero_buscado, " no esta en la lista")

    resp = input("Desea buscar otro número (s/N): ")
    if resp.upper() == "S":
        ciclo = True
