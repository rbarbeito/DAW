# Dado a un array de char y un carácter c el siguiente método cuenta el número de
#   apariciones de c en a. Por ejemplo, si a es {'g','g','a','c','t','g','a'} y c es
#   'g' el método devuelve 3.

lista=['g','g','a','c','t','g','a']

a=input("Defina la letra a buscar: ")
##count=0
lista1=[i for i in lista if i==a]
##    if i==a:
##        count+=1
        
print("Ocurrencias de "+ a + ": " + str(len(lista1)))
    
