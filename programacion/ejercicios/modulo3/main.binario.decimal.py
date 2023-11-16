binario = input("Teclea tu número binario: ")
invertido = ""
potencia = 0
suma = 0
for i in binario:
    invertido = i+invertido
for i in invertido:
    if i == "1":
        suma = suma + (2**potencia)
    potencia += 1

print(suma)
