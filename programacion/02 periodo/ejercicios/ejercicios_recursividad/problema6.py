# Problema 6 - Suma componentes
#   Dado a un array de int los siguientes métodos devuelven un array del mismo tamaño que a, tal
#   que la componente i del resultado contiene la suma de las componentes en a[0...i]
#   Por ejemplo, si a = {1 4 2 1 0 3} devuelven el array {1 5 7 6 6 9}

lista=[1, 4, 2, -1, 0, 3]

##print("Creando la lista inicial")

# while True:
#     try:
#         a=int(input("Teclee número que ser adicionado (-1 para fin): "))
#         if a == -1:
#             break
        
#         list.append(a)
        
#     except ValueError:
#         print("\nSolo se aceptan números")
    

if len(lista) !=0: 
    nueva_lista=lista[:]
    
    for i in range(1,len(lista)):
        nueva_lista[i]=nueva_lista[i-1]+lista[i]
        
print(nueva_lista)
