palabra=input("Teclee una palabra (chupacabra para terminar): ")

contador=0

while True:
    contador += 1
    if palabra == "chupacabra":
        break
    palabra=input("Teclee una palabra (chupacabra para terminar): ")
    
print("¡Has dejado el bucle con éxito.", "Tecleaste " + str(contador - 1)+ " palabras diferentes")