margen_izquierdo = 4
titulo = 0
bd_clientes={}


opciones_menu = ["GESTIÓN BASE DATOS - CLIENTES", "MENÚ",
                 "1. Adicionar cliente",
                 "2. Eliminar cliente",
                 "3. Mostrar cliente",
                 "4. Listar clientes",
                 "5. Listado clientes preferentes",
                 "0. Salir"]

datos_clientes=["NIF","nombre","dirección","teléfono","correo","preferente"]



x_menu = -1
while x_menu != 0:

    for m in range(len(opciones_menu)):
        if titulo < len(opciones_menu[m]):
            titulo = len(opciones_menu[m])

    long = titulo + margen_izquierdo * 2
    long_titulo = (long-len(opciones_menu[0]))//2
    long_titulo_menu = (long-len(opciones_menu[1]))//2

    print()
    print("*"*long)
    print(" "*long_titulo + opciones_menu[0])
    print(" "*long_titulo_menu + opciones_menu[1])
    print("*"*long)
    for m in range(2, len(opciones_menu)):
        print(" "*margen_izquierdo + opciones_menu[m])
    print("*"*long)

    x_menu = input("Seleccione acción: ")

    if x_menu == '':
        print("Opción no valida")
        continue
    
    print()
    
    if x_menu=="0":
        print("\nFin del programa, Adios!!")
        break
    
    elif x_menu == "1":
        id=""
        for i in range(len(datos_clientes)):
            
            texto="Teclee el "+ datos_clientes[i]+ " del cliente"
            if i == len(datos_clientes)-1:
                texto+="(T/F)"
            texto+=": "
            
            dato=input(texto)
            if i==0:
                id=dato
                bd_clientes[id]={}
            else:
                bd_clientes[id][datos_clientes[i]]= dato
                
    
    elif x_menu == "2":
        nif= input("Teclee el " + datos_clientes[0] + " del cliente a borrar: ")
        
        if nif not in bd_clientes.keys():
            print("Cliente no registrado en la base de datos")
            continue
        
        del bd_clientes[nif]
        print("Cliente Borrado")
            
            
    elif x_menu == "3":
        nif= input("Teclee el " + datos_clientes[0] + " del cliente a consultar: ")
            
        if nif not in bd_clientes.keys():
            print("Cliente no registrado en la base de datos")
            continue
        
        for key,value in bd_clientes[nif].items():
                print(key,"=>", value)
            
                
    elif x_menu=="4":
        if len(bd_clientes)==0:
            print("No existen registros de clientes")
            continue
        
        for key,value in bd_clientes.items():
            print("NIF =>", key)
            for llave, valor in value.items():
                print(llave, "=>", valor)
            print()
        
    elif x_menu=="5":
        count=0
        
        for key,value in bd_clientes.items():
            if value["preferente"]=="T" or value["preferente"]=="t":
                print(value["nombre"])
                count+=1
        
        if count==0:
            print("No existen clientes preferentes")
            continue
        
                
            