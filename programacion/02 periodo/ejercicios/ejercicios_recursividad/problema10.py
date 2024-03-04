####Dado a un array de char y un char c, el siguiente método escribe en la salida
####estándar los sucesivos prefijos de a, de más corto a más largo, que no
####contienen el carácter c.

##def funcAsig(n):
##    a = [0 for x in range(14)]
##
##    inicio = 0
##    long = len(a)
##
##
##    while long > 0:
##        inicio += 1
##
##        if long % 2 == 0:
##            final = long//2 - 1
##        else:
##            final = long//2
##
##       
##
##       
##
##    print(lista)

   
def asigSuc(n):
    a=[0 for i in range(n)]
    print(a)

    
    ini=0
    fin=len(a)-1
    
    valor=1

    while ini <= fin:
        a[ini] = valor
        medio=(ini+fin)//2
        
        print("Medio:", medio)
        ini = medio +1
        print("Siguiente", ini)
        valor += 1
        print(a)

    print(a)
        
asigSuc(10000)    
    
    
    


    

