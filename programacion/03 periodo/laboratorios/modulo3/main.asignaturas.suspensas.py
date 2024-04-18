# ejercicio 4
margen_izquierdo = 4
titulo = "ELIMINAR ASIGNATURAS APROBADAS"
long = len(titulo)+margen_izquierdo*2
print()
print("*"*long)
print(" "*margen_izquierdo + titulo)
print("*"*long)


aprob = int(input("¿Cuál es mínimo a obtener para aprobar?: "))
asignaturas = []
notas = []
string_asignaturas = ""

while True:
    asig = input("Entre el nombre de la asignatura o 'Salir' para terminar: ")
    if asig.upper() == "SALIR":
        break

    text = "Teclee la nota de " + asig + ": "
    nota = int(input(text))

    if nota < aprob:
        asignaturas.append(asig)

if len(asignaturas) != 0:
    i = len(asignaturas)
    print("Usted debe repetir: ")
    while i > 1:
        print(asignaturas[i-1], end=", ")
        i -= 1

    print(asignaturas[i-1], end=" ")
else:
    print("Usted aprobó el curso satisfactoriamente")
