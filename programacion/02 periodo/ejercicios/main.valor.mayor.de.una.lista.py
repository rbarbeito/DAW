# Encontrar el valor mayor de una lista

list = []
ciclo = True


while True:
    numero = int(input("Adcione su número a la lista, -1 para terminar: "))

    if numero == -1:
        break
    else:
        list.append(numero)


while ciclo:
    ciclo=False
   
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            ciclo=True
            
total=0
for i in range(len(list)-1):
    total+=list[i]    

print("El numero mayor de la lista es", list[len(list)-1])
print("El numero menor de la lista es", list[0])
print("El promedio es", round(total/len(list),2))