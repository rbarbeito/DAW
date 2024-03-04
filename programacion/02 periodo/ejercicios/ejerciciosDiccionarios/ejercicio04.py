asignaturas={}

while True:
    
    asig=input("Teclee nombre de la asignatura: ")
    
    if asig == '':
        break
    
    crédito= int(input("Teclee la cantidad de créditos(1-10) de " + asig +" :"))
    
    if crédito not in range(1,11):
        print("El programa se termina por error, debió teclear los créditos validos")
        break    
    
    asignaturas[asig]=crédito


if len(asignaturas)!=0:
    
    total=0
    print()
    for asig in asignaturas:
        
        if asignaturas[asig] >1:
            credit="créditos"
        else:
            credit="crédito"
            
        total+=asignaturas[asig]
        
        print(asig, "tiene" ,asignaturas[asig], credit)
    
    print("El numero total de créditos del curso es:", total)