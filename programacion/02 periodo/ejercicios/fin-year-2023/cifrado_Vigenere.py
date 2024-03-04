

alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
matriz_alpha = []


for x in range(len(alphabet)):
    matriz_alpha.append(alphabet[x:]+alphabet[:x])


# Define la cantidad de caracteres validos con los que cuenta la cadena de texto a encriptar


def count_case(mensaje):
    contador = 0

    for i in range(len(mensaje)):
        if mensaje[i].upper() in alphabet:
            contador += 1

    return contador


# generates the key you will use for encryption
def generating_clave(clave):
    contador = count_case(mensaje)

    if len(clave) > contador:
        clave = clave[:contador]
    elif len(clave) < contador:
        while len(clave) < contador:
            for i in range(len(clave)):
                clave += clave[i]
                if len(clave) >= contador:
                    break

    return clave

# Defining coding signal


def signal_codification(clave, key_position):
    signal = ""

    for i in range(len(matriz_alpha)):
        if matriz_alpha[i][0] == clave[key_position].upper():
            signal = matriz_alpha[i]

    return signal


# Message coding function
def cod_vig(message, clave):
    message_encrypted = ""
    clave = generating_clave(clave)
    key_position = 0

    for m in range(len(message)):

        if message[m].upper() not in alphabet:
            message_encrypted += message[m]
        else:
            signal = signal_codification(clave, key_position)
            key_position += 1

            for s in range(len(alphabet)):
                if message[m].upper() == alphabet[s]:
                    message_encrypted += signal[s]

    return message_encrypted


def dec_vig(message, clave):
    message_unencrypted = ""
    clave = generating_clave(clave)
    key_position = 0

    for m in range(len(message)):
        if mensaje[m].upper() not in alphabet:
            message_unencrypted += message[m]
        else:
            signal = signal_codification(clave, key_position)
            key_position += 1

            for s in range(len(signal)):
                if message[m].upper() == signal[s]:
                    message_unencrypted += alphabet[s]

    return message_unencrypted


menu = -1
while menu != 0:

    print("\n")
    print("Menú - CIFRADO VIGENERE")
    print("1. Encriptar mensaje")
    print("2. Desencriptar mensaje")
    print("0. Salir")
    print()
    menu = int(input("¿Que desea hacer?: "))
    print()

    if menu == 1:
        mensaje = input("Teclee el mensaje a encriptar: ")
        clave = input("Teclee la clave de cifrado: ")

        print("\nMensaje en texto plano: ", mensaje)
        print("Mensaje encriptado: ", cod_vig(mensaje, clave))

    elif menu == 2:
        mensaje = input("Teclee el mensaje a desencriptar: ")
        clave = input("Teclee la clave de cifrado: ")

        print("\nMensaje encriptado: ", mensaje)
        print("Mensaje desencriptado: ", dec_vig(mensaje, clave))
