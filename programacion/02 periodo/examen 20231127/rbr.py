margen_izquierdo = 4
titulo = 0
lista_num = []

opciones_menu = ["EXAMEN DE PROGRAMACIÓN (27-11-2023)", "MENÚ (SECCIÓN 1)",
                 "Teclee el numero del ejercicio del 1 al 35",
                 "0. Salir"]


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

    x_menu = int(input("Seleccione el ejercico: "))

    print()

    if x_menu == 1:
        nombre_usuario=input("Ingrese su nombre: ")
        print("Ahora estás en el examen de programación,", nombre_usuario)

    elif x_menu ==2:
        nombre_usuario=input("Ingrese su nombre: ")
        print("Tu nombre:", nombre_usuario,"\nAhora estás en el examen de programación,", nombre_usuario,"\n", " "*4,"Despeja tu mente y se 'ZEN'\n", " "* 10, "Todo saldrá bien", nombre_usuario, sep=" ")

    elif x_menu == 3:
        numero_uno=int(input("Teclee el primer número: "))
        numero_dos=int(input("Teclee el segundo número: "))
        print("Valores: "+ str(numero_uno) + ", " + str(numero_dos) +"\nLa suma de " + str(numero_uno) + " + "+ str(numero_dos) + " = " + str(numero_uno + numero_dos))

    elif x_menu ==4:
        numero_uno=int(input("Ingrese un número: "))
        numero_dos=int(input("Ingrese otro número: "))
        suma=numero_uno + numero_dos
        print("Suman: "+str(suma))
        numero_tres=int(input("Ingresa un nuevo número: "))
        print("Multiplicación de la suma por el último número: " + str(suma*numero_tres))
        
    elif x_menu == 5:
        temp_farenheit=float(input("Ingresar una temperatura en Farenheit: "))
        temp_celcius=(5/9)*(temp_farenheit-32)
        print(str(temp_celcius))
        
    elif x_menu == 6:
        numero_uno=float(input("Primer número: "))
        numero_dos=float(input("Segundo número: "))
        numero_tres=float(input("Tercer número: "))
        print("El promedio de los tres es "+str(round((numero_uno+numero_dos+numero_tres)/3 , 2)))

    elif x_menu == 7:
        numero=int(input("Número entero: "))
##        if numero%2==0:
##            print(True)
##        else:
##            print(False)
        print(numero%2==0)

    elif x_menu == 8:
        cadena=input("Ingresa una frase: ")
##        if len(cadena)%2 == 0:
##            print(False)
##        else:
##            print(True)
        print(len(cadena)%2 == 0)
            
    elif x_menu==9:
        edad_user=int(input("Tu edad: "))
        art_user=int(input("Artículos comprados: "))

##        if edad_user >= 18:
##            if art_user > 1:
##                print(True)
##            else:
##                print(False)
##        else:
##            print(False)

        print(edad_user >= 18 and art_user > 1 )

    elif x_menu == 10:
        nombre_uno=input("Tu nombre: ")
        nombre_dos=input("Otro nombre: ")

##        if nombre_uno[0] == nombre_dos[0] or  nombre_uno[len(nombre_uno)-1] == nombre_dos[len(nombre_dos)-1]:
##            print(True)
##        else:
##            print(False)
        print(nombre_uno[0] == nombre_dos[0] or  nombre_uno[len(nombre_uno)-1] == nombre_dos[len(nombre_dos)-1])

    elif x_menu == 11:
        text_user=input("Ingresa un texto: ")
        print("El carácter en primer lugar es:", text_user[0])
        position_user=int(input("Ingresa un número menor que " + str(len(text_user)) + ": "))
        print("El carácter en esa posición es:", text_user[position_user+1])

    elif x_menu==12:
        palabra_uno=input("Una palabra: ")
        palabra_dos=input("Otra palabra: ")
              

##        if ord(palabra_uno[0]) < ord(palabra_dos[0]):
##           print(True)
##        else:
##            print(False)

        print(palabra_uno < palabra_dos)  
            
    elif x_menu==13:
        valores=input("Valores: ")
        position =0
        for i in range(len(valores)):
            if valores[i]==",":
                position = i
                            
        if valores[:position] > valores[position+1:]:
            print(valores[:position], "es menor que", valores[position+1:])
        else:
             print(valores[:position], "es mayor que", valores[position+1:])

    elif x_menu==14:
        valor=input("Valor: ")
                                  
        if valor >= 0 and valor <=10:
            print("Esta entre 0 y 10")
        else:
            print("No esta entre 0 y 10")

    elif x_menu==15:
        valor=input("Valor: ")
                                  
        if valor >= 0 and valor <=10:
            print("Esta entre 0 y 10")
        elif valor > 10 and valor <=20:
            print("Esta entre 11 y 20")
        elif valor > 20 and valor <=30:
            print("Esta entre 21 y 30")
        else:
            print("No esta en los rangos especificados")

    elif x_menu==16:
        num=0

        while num<=100:
            print(num, end=" ")
            num+=1

    elif x_menu==17:
        
        for i in range(100):
            print(i+1, end=" ")
            
    elif x_menu==18:
        
        for i in range(1,101):
            if i%2 == 0:
                print(i, end=" ")

    elif x_menu==19:
        texto="Hola mundo"
        for i in texto:
            print(i,end="*")

    elif x_menu==20:
        list=[rango(10)]
##        for i in range(11):
##            list.append(i)
##
        print(list)

    elif x_menu==21:
        list=[]
        contador=10
        while contador>=0:
            list.append(contador)
            contador-=1

        print(list)

    elif x_menu==22:
        list=[]
        cadena=input("Teclee su cadena de texto: ")
        for i in range(len(cadena)):
            list.append(i)

        print(list)

    elif x_menu==23:
        list_uno=[]
        list_dos=[]
        for i in range(11):
            list_uno.append(i)
        for i in range(15,21):
            list_dos.append(i)

        print("Lista uno: ", list_uno)
        print("Lista dos: ", list_dos)
        print("Lista completa: ", list_uno + list_dos)

    elif x_menu==24:
        cadenas=input("Introduzca dos cadenas separadas por coma: ")
        position=0

        for i in range(len(cadenas)):
            if cadenas[i]==",":
                position = i

        print(cadenas[position+1:position+3]  + cadenas[2:position]+ " "+cadenas[:2] + cadenas[position+3:])


    elif x_menu==25:
        letra=input("Introdizca una letra: ")
        vocales=["A","E", "I","O","U","a","e","i","o","u"]
        
        if len(letra)>1:
            print("No se puede procesar el dato")
        elif letra in vocales:
            print("Es una vocal")
        else:
            print("No es una vocal")


    elif x_menu==26:
        ciclo= True
        list=[]

        while ciclo:
            numero=input("Teclee un numera a su lista ('S' para salir): ")
            if numero == 's' or numero == 'S':
                break
            else:
                list.append(int(numero))

        while ciclo:
            ciclo=False
   
            for i in range(len(list)-1):
                if list[i] > list[i+1]:
                    list[i], list[i+1] = list[i+1], list[i]
                    ciclo=True
            
        

        print("Menor:", list[0])

    elif x_menu==27:
        suma=0
        numero=int(input("Hasta que numero quieres sumar: "))

        for i in range(numero+1):
            suma+=i
            
        print(suma)


    elif x_menu==28:
        vocales=["A","E", "I","O","U","a","e","i","o","u"]
        suma_vocales=0
        frase=input("Diga su frase")

        for i in range(len(frase)):
            
            if frase[i] in vocales:
                suma_vocales+=1
            
        print("Su frase tiene:", suma_vocales, "y", len(frase)-suma_vocales, "consonantes")

        
    elif x_menu==29:
        user=input("Teclee su usuario: ")
        password=input("Teclee su contraseña: ")

        if user=="Lancelot" and password=="excalibur":
            print("Usuario y contraseña correcto. Puede ingresar a Camelot")
        else:
            print("Acceso denegado")


    elif x_menu==30:
        numero=int(input("Teclee su numero: "))
        valor=0

        while valor < numero:
            valor+=1
            print(valor)


    elif x_menu==31:
        cadena=input("Teclee una cadena: ")
        contador=0

        for i in range(len(cadena)//2):
            if cadena[i] != cadena[len(cadena)-i-1]:
                contador+=1

        if contador==0:
            print("La cadena es palindromo")
        else:
            print("La cadena no es palindromo")





    elif x_menu==32:
        numero=int(input("Teclee una numero: "))
        valor=0

        print("Número: ",numero)
        print("Divisores")

        while valor < numero:
            valor+=1
            if numero%valor==0:
                print(valor)
       
       
    elif x_menu==33:
        vocal=input("ingresa una vocal: ")
        texto=input("Ingrese una frase: ")

        contador=0
        print("Vocal: ", vocal)

        for i in range(len(texto)):
            if texto[i]==vocal:
                contador=i+1
                break

        print(contador)

    elif x_menu==34:
        lista_uno=[2,5,1,8]
        lista_dos=[3,1,6,7]

        lista=[]

        for i in range(len(lista_uno)):
            lista.append(lista_uno[i] > lista_dos[len(lista_uno)-i-1])

        print(lista)
                   

        

    elif x_menu==35:
        control=True
        lista_nombres=[]
        lista_unicos=[]
        lista_contador=[]

        while control:
            control=False
            nombre=input("Introduzca el nombre, (-1 para terminar): ")
            if nombre!="-1":
                control=True
                lista_nombres.append(nombre)

        lista_unicos.append(lista_nombres[0])

        for i in range(len(lista_nombres)):
            if lista_nombres[i] not in lista_unicos:
                lista_unicos.append(lista_nombres[i])

        for i in range(len(lista_unicos)):
            contador=0
            for x in range(len(lista_nombres)):
                if lista_unicos[i] == lista_nombres[x]:
                    contador+=1
            lista_contador.append(contador)

        for i in range(len(lista_unicos)):
            print(lista_unicos[i] + ": " + str(lista_contador[i]))
           
    else:
        print("Fin de la sección, Adios!!")
        break
