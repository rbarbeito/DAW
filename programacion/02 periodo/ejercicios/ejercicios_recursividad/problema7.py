####Dado a un array de char, el siguiente método escribe en la salida estándar los
####sucesivos prefijos de a, de más corto a más largo.


a = [ 'a', 'b', 'c', 'd', 'e' ]


    
for i in range(1,len(a)+1):
    concatenar=''
    for x in a[:i]:
        concatenar+=x

    print(concatenar)

 
        

    
