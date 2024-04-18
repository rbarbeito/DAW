# ejercicio 3
margen_izquierdo = 4
titulo = "NOTA EN CADA ASIGNATURA"
long = len(titulo)+margen_izquierdo*2
print()
print("*"*long)
print(" "*margen_izquierdo + titulo)
print("*"*long)
asignaturas = []
notas = []


while True:
    asig = input("Entre el nombre de la asignatura o 'Salir' para terminar: ")
    if asig.upper() == "SALIR":
        break
    asignaturas.append(asig)

if len(asignaturas) > 0:
    for i in asignaturas:
        text = "Teclee la nota de " + str(i) + ": "
        nota = int(input("Teclee la nota de " + str(i) + ": "))
        notas.append(nota)

    suma = 0
    for i in range(len(asignaturas)):
        print("En", asignaturas[i], "has sacado", str(notas[i]))
        suma += notas[i]

    if suma > 0:
        print("Tu promedio es:", round(suma/len(asignaturas), 2))
