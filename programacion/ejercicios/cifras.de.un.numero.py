# comprobar las cifras de un numero(enteros!!!!)
while True:
    try:
        a = int(input("Entre el numero base: "))

        if a <= 0:
            print("El numero debe ser mayor que cero")
            continue
        else:
            break

    except ValueError:
        print("El valor debe ser un numero")

while True:
    try:
        b = int(input("Entre el numero a buscar: "))

        if b < 0 and b > 9:
            print("El numero debe ser mayor que cero y menor que nueve")
            continue
        else:
            break

    except ValueError:
        print("El valor debe ser un numero")


count = 0
primario=a

while a != 0:
    if a % 10 == b:
         count+=1
    a//=10     
    

if count==0:
    print("El numero", b, "no se encuentra en", primario)
elif count ==1:
    print("El numero", b , "se encuentra", count,"vez en", primario)
elif count>1:
    print("El numero", b , "se encuentra", count,"veces en", primario)



