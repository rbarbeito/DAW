def decimal_to_binario(valor, binario):
    if valor == 0:
        return binario

    binario += valor % 2
    return decimal_to_binario(valor//2, binario)


def separar_valores(numero):
    octetos = []

    for i in numero:
        if i != '.':
            valor += i
        else:
            octetos.append(valor)
            valor = ''
    octetos.append(valor)

    return octetos


def convertir_mascara(mascara):
    valor = ''
    octetos = separar_valores(mascara)

    mascaraBits = 0
    for i in octetos:
        mascaraBits += decimal_to_binario(int(i), 0)

    return mascaraBits


def calcular_bits_necesarios(host, bits):
    if host <= 2**bits:
        return bits

    return calcular_bits_necesarios(host, bits+1)


# ip=input("Cuál es su numero ip?: ")
# mascara=input("Cuál es su mascara de red?: ")
# host=input("¿Cuantos Host necesitas en tu red?: ")
ip = "192.168.1.0"
mascara = "255.255.255.0"
host = "15"

try:
    host = int(host)
except ValueError:
    print("El valor introducido no es un número")

if len(mascara) > 2:
    mascara = convertir_mascara(mascara)


try:
    mascara = int(mascara)
except ValueError:
    print("El valor de la mascara no es un número")

bits_de_host = calcular_bits_necesarios(host, 0)
bits_de_red = 8 - bits_de_host
mascara += bits_de_red
magic_number = 2**bits_de_host

ip_lista = separar_valores(ip)

for i in range(bits_de_red):
    print(ip_lista[0]+"."+ip_lista[1]+"."+ip_lista[2]+"."+str(int(ip)))


# redInicial = datosRed(ip, mascara)
