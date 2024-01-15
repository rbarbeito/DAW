vocabulario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
no_cifrado=0


######Esta funcion busca la position de la letra en el dicioniario
def buscar_position(letra):
    position="null"
    for i in range(len(vocabulario)):
        if vocabulario[i] == letra.upper():
            position= i
            
    return position

######Cifra el mensaje segun el salto de cifrado definido
def cifrar_mensaje(letra):
    position = buscar_position(letra)
    
    if position != "null":
        position += no_cifrado
        
        if position > len(vocabulario)-1:
            position -= len(vocabulario)     

    return position
    
######Descifra el mensaje segun el salto definido
def descifrar_mensaje(letra):
    position= buscar_position(letra)
    
    if position!="null":
        position-=no_cifrado

        if position < 0:
            position += len(vocabulario)
            
    return position



menu=-1
while menu!=0:


    print("\n")
    print("Menú")
    print("1. Encriptar mensaje")
    print("2. Desencriptar mensaje")
    print("3. Fuerza bruta")
    print("0. Salir")
    print()
    menu = int(input("¿Que desea hacer?: "))
    print()

    if menu == 1:
        mensaje = input("Teclee el mensaje a encriptar: ")
        no_cifrado=int(input("Defina el valor de cifrado(1-10): "))

        print("Mensaje encriptado: ", end="")
        
        for i in range(len(mensaje)):
            letra=mensaje[i]
            pos=cifrar_mensaje(letra)
            
            if  pos != "null":
                letra=vocabulario[pos]
                
            print(letra, end="")

    elif menu == 2:
        mensaje= input("Teclee el mensaje a desencriptar: ")
        no_cifrado=int(input("Defina el valor de cifrado(1-10): "))

        print("Mensaje desencriptado: ", end="")

        for i in range(len(mensaje)):
            letra=mensaje[i]
            pos = descifrar_mensaje(letra)
            
            if  pos != "null":
                letra=vocabulario[pos]
                
            print(letra, end="")

    elif menu == 3:
        mensaje = input("Teclee el mensaje cifrado: ")

        for no_cifrado in range(1,11):
            print("\nMensaje con codificacion ", no_cifrado, ": ", sep="", end="")
            for i in range(len(mensaje)):
                letra=mensaje[i]
                pos = descifrar_mensaje(letra)

                if pos!="null":
                    letra= vocabulario[pos]
                print(letra, end="")
            


    
   
