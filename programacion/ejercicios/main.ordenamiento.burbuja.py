list = []


while True:
    numero = int(input("Adcione su número a la lista, -1 para terminar: "))

    if numero == -1:
        break
    else:
        list.append(numero)

print(list)
print()

while True:
    movimientos = 0
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            movimientos += 1

    if movimientos == 0:
        break

print(list)
