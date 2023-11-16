# Encontrar el valor mayor de una lista

list = [17, 3, 11, 5, 1, 9, 7, 15, 13]


ciclo = True

while ciclo:
    ciclo=False
   
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            ciclo=True
            
print("El numero mayor de la lista es", list[len(list)-1])