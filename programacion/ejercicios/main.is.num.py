num=input("Teclee su numero: ")
contar=0

for i in range(len(num)):
    if num[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
            contar+=1

if contar!=0:
    print("No es un número válido")
else:
    print("Es un número válido")