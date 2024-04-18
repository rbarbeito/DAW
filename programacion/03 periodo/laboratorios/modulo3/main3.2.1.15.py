numero=int(input("Número a comprobar: "))
count=0

if numero<=0:
    print("El número no puede ser negativo ni igual a cero")
else: 
    while numero != 1:
        count+=1
        if numero % 2 == 0:
            numero=numero/2
        else:
            numero=3*numero+1
        
        print(numero)
    
    print("pasos = " +str(count))
    