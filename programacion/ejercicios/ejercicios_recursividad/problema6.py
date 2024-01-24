# Problema 6 - Suma componentes
#   Dado a un array de int los siguientes métodos devuelven un array del mismo tamaño que a, tal
#   que la componente i del resultado contiene la suma de las componentes en a[0...i]
#   Por ejemplo, si a = {1 4 2 1 0 3} devuelven el array {1 5 7 6 6 9}

list=[1 ,4 ,2, 1, 0 ,3]

print("Creando la lista inicial")

# while True:
#     try:
#         a=int(input("Teclee número que ser adicionado (-1 para fin): "))
#         if a == -1:
#             break
        
#         list.append(a)
        
#     except ValueError:
#         print("\nSolo se aceptan números")
    

if len(list) !=0: 
    nueva_list=list[:1]
    
    print(list)
    
    for i in range(2,len(list)+1):
        sum=0
        for x in range(0,i):
            sum+=list[x]
            
        nueva_list.append(sum)
        
print(nueva_list)
