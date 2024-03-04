####Dado a un array de char y un char c, el siguiente método escribe en la salida
####estándar los sucesivos prefijos de a, de más corto a más largo, que no
####contienen el carácter c.


a = ['a', 'l', 'a', 'm', 'e', 'd', 'a' ]

c = 'a'


    
for i in  range(len(a)):
    concatenar=''
           
    for x in a[:i+1]:
       concatenar += x

    if concatenar[0] == concatenar[i]:
        print(concatenar)
