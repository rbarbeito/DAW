import random
print("RULETA RUSA")

numero_jugador=int(input("Escoja el lugar a sentarse(1-4): "))

while numero_jugador<1 or numero_jugador>4:
    print("Esta escojiendo un número fuera de rango\n")
    numero_jugador=int(input("Escoja el lugar a sentarse(1-4): "))

numero_random=random.randint(1, 4)
contador_supervivencia=0

while numero_jugador!=numero_random:
    contador_supervivencia=contador_supervivencia+1

    if contador_supervivencia==1:
        texto_vez="vez"
    else:
        texto_vez="veces"


    print("Sobreviviste",contador_supervivencia , texto_vez, "\n")
    eleccion=input("¿Quieres volver a tentar tu suerte? (s/n): ")


    while eleccion.upper() != "S" and eleccion.upper() != "N":
        eleccion=input("Error en respuesta, ¿Quieres volver a tentar tu suerte? (s/n): ")
  

    if eleccion.upper() != "S":
        print("\nLograste sobrevivir " +  str(contador_supervivencia), texto_vez+ ". Regresa cuando quieras")
        break

    numero_random=random.randint(1,4)

if contador_supervivencia==1:
    texto_vez="vez"
else:
    texto_vez="veces"

if contador_supervivencia==0:
    print("Hoy no has tenido suerte, fuiste muy valiente al intentarlo, perdiste en el primer intento")

