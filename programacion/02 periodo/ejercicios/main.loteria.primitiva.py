# Ejercicio 1
margen_izquierdo = 4
titulo = "LOTERIA PRIMITIVA"
long = len(titulo)+margen_izquierdo*2
print()
print("*"*long)
print(" "*margen_izquierdo + titulo)
print("*"*long)

list_loteria = []
for i in range(6):
    num = int(input("Entre el numero ganador de la loteria: "))
    list_loteria.append(num)

    for x in range(len(list_loteria)):
        if list_loteria[i] < list_loteria[x]:
            list_loteria[i], list_loteria[x] = list_loteria[x], list_loteria[i]

print(list_loteria)
