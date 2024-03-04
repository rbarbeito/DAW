####Dado a un array de char y un char c, el siguiente método escribe en la salida
####estándar los sucesivos prefijos de a, de más corto a más largo, que no
####contienen el carácter c.


a = [ 'e', 'j', 'e', 'm', 'p', 'l', 'o' ]

c = 'm'


    
for i in  range(len(a)+1):
    concatenar=''
        
    if a[i] == c:
        break
        
    for x in a[:i+1]:
        concatenar += x

    print(concatenar)
