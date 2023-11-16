numero = int(input("Teclee tu número decimal: "))
binario = ""

while numero != 0:
    resto = str(numero % 2)
    numero = numero//2
    binario = resto+binario

print(binario)
