import random
import time

EMPTY=" "

board=[]
jugadores=[]
fichas=['X','O']

columnas=[]
for i in range(1,8):
    columnas.append(''+ str(i) + '')

jugadores=[input("Diga el nombre el jugador: ") for i in range(2)]

cuatro=True
seguir_jugando=True

print("\nComienza jugando", end="")

while seguir_jugando:
    seguir_jugando=False

    cantidad_mov=42

    board=[[EMPTY for i in range(7)] for j in range(6)]

    comienza=random.randint(0,100)
    if comienza%2 == 1:
        jugadores[0],jugadores[1]=jugadores[1],jugadores[0]


    

    for i in range(5):
        time.sleep(1)
        print(".",end="")

    
    print(" ",jugadores[0],"\n")

    
    print(columnas)
    for i in range(len(board)-1,-1,-1):
        print(board[i])




    
    while cuatro:
        columna=0
        ficha_seleccionada=fichas[0]

        print()
        
        columna=int(input("Selecciona tu columna "+jugadores[0] +" : "))
        print()

        if columna >= 1 and columna <= 7:

            columna-=1
            cantidad_mov-=1

            for i in range(6):
               if board[i][columna] == ' ':
                   board[i][columna]=fichas[0]
                   fichas[0],fichas[1]=fichas[1],fichas[0]
                   break;

            print(columnas)
            for i in range(len(board)-1,-1,-1):
                print(board[i])


            print()
            
#### control de las ganadas verticales 
            for c in range(6):
                seguidos=[1 for i in range(7)]
                for f in range(5):
               
                    if board[f][c]  == board[f+1][c] == ficha_seleccionada:
                        seguidos[c]+=1
                        
                        if 4 in seguidos:
                            print("Ha ganado", jugadores[0],"con una linea vertical")
                            cuatro=False
                            break
                        
                    elif board[f][c] != board[f+1][c]:
                        seguidos[c]=1
                        
                    
#### control de las ganadas horizontales
            for f in range(6):
                seguidos=[1 for i in range(6)]
                for c in range(6):
               
                    if board[f][c]  == board[f][c+1] == ficha_seleccionada:
                        seguidos[f]+=1
                        
                        if 4 in seguidos:
                            print("Ha ganado", jugadores[0] , "con una linea horizontal")
                            cuatro=False
                            break
                        
                    elif board[f][c] != board[f][c+1]:
                        seguidos[f]=1
                        

#### control de las ganadas inclinadas ascendentes
            seguidos=[1 for i in range(7)]
            for f in range(5):
                for c in range(6):

                    if board[f][c] == board[f+1][c+1] == ficha_seleccionada:         
                        seguidos[c+1]=seguidos[c]+1

                        if 4 in seguidos:
                            print("Ha ganado", jugadores[0], "con una linea inclinada ascendente")
                            cuatro=False
                            break
                        

#### control de las ganadas inclinadas descendentes
            seguidos=[1 for i in range(7)]
            for f in range(5):
                for c in range(6):

                    if board[f][c] == board[f+1][c-1] == ficha_seleccionada: 
                        seguidos[c-1]=seguidos[c]+1

                        if 4 in seguidos:
                            print("Ha ganado", jugadores[0]," con una linea inclinada descendente")
                            cuatro=False
                            break

                        print(seguidos)



                   

            if cantidad_mov == 0:
                print("Es un empate")
                cuatro=False
    

            jugadores[0],jugadores[1]=jugadores[1],jugadores[0]

        else:
            print("El número de columna debe estar en el rango de 1 a 7")
            continue

    jugar=input("¿Desea seguir jugando? (s/N): ")

    if jugar == "s" or jugar == "S":
        seguir_jugando = cuatro = True
        

print("¡Hasta la vista, Baby!")
    
    
        
    

