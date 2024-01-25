####Dado a un array de char y un char c, el siguiente método escribe en la salida
####estándar los sucesivos prefijos de a, de más corto a más largo, que no
####contienen el carácter c.

a = [0 for x in range(100)]
lista = []

inicio = 0
long = len(a)


while long > 0:
    inicio += 1

    if long % 2 == 0:
        tamano = long//2 - 1
    else:
        tamano = long//2

    long //= 2

    lista += [inicio] + [0 for x in range(tamano)]

print(lista)

   

    
    
    


    

