# Problema 5 - Repetición de caracteres

#   Dado a un array de char y un carácter c el siguiente método comprueba si c aparece
#   repetido en a Por ejemplo, si a es {'g','g','a','c','t','a','g','a'} y c es
#   'a' el método devuelve true. Para el mismo array, si c es 't' el método devuelve false.

list=['g','g','a','c','t','a','g','a']

count=0

a=input("Carácter a buscar: ")

for i in list:
    if a==i:
        count+=1

    if count>1:
        break

print(count>1)