# Dado a un array de char y un carácter c el siguiente método cuenta el número de
#   apariciones de c en a. Por ejemplo, si a es {'g','g','a','c','t','g','a'} y c es
#   'g' el método devuelve 3.

list=['g','g','a','c','t','g','a']

a=input("Defina la letra a buscar: ")
count=0
for i in list:
    if i==a:
        count+=1
        
print("Ocurrencias de "+ a + ": " + str(count))
    