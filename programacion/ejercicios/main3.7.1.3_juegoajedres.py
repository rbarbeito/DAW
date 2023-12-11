EMPTY = "-"

W_PEON = "♟"
W_TORRE = "♖"
W_CABALLO = "♘"
W_REY="♔"
W_DAMA="♕"
W_ALFIL="♗"

B_REY="♚"
B_DAMA="♛"
B_TORRE="♜"
B_ALFIL="♝"
B_CABALLO="♞"
B_PEON="♟"

letras=["A","B","C","D","E","F","G","H"]
fichas=["TORRE","CABALLO","ALFIL","DAMA","REY","PEON"]

jugar=True
fin_juego=["jm","JM","jM","Jm"]
turno_lista=[["W_","Blancas"],["B_","Negras"]]

board = []
historial_partida=[]
turno=[]

board = [[EMPTY for i in range(8)] for j in range(8)]

board[0][0] = W_TORRE
board[0][7] = W_TORRE
board[0][1] = W_CABALLO
board[0][6] = W_CABALLO
board[0][2] = W_ALFIL
board[0][5] = W_ALFIL
board[0][3] = W_DAMA
board[0][4] = W_REY

board[7][0] = B_TORRE
board[7][7] = B_TORRE
board[7][1] = B_CABALLO
board[7][6] = B_CABALLO
board[7][2] = B_ALFIL
board[7][5] = B_ALFIL
board[7][3] = B_DAMA
board[7][4] = B_REY

for i in range(8):
    board[1][i]=W_PEON
    board[6][i]=B_PEON


   
for i in range(8,0,-1):
    print(i,board[i-1])

print(" ",letras) 


print("\nLas casilla se definen de esta forma (Pa2)")
print("Donde P - ficha en este caso es 'PEÓN' a4 ")


while jugar:

    print("\nEs el turno de las", turno_lista[0][1])

    orig=input("\n¿Qué ficha quiere mover?: ")

    if orig in fin_juego:   
        break
        
    dest=input("¿A donde quiere moverlo?: ")

    turno.append(orig[0]+dest)

    if len(turno) != 2:
        historial_partida.append(turno)
    elif turno_lista[0][1] != "Blancas":
        turno=[]
   

    pos_orig=0
    pos_dest=0
    for i in range(len(letras)):
        if letras[i].upper() == orig[1].upper():
            pos_orig=i

        if letras[i].upper()== dest[0].upper():
            pos_dest=i
            
    if board[int(dest[1])-1][pos_dest] == EMPTY:
        board[int(orig[2])-1][pos_orig],board[int(dest[1])-1][pos_dest]=board[int(dest[1])-1][pos_dest],board[int(orig[2])-1][pos_orig]
    else:
        board[int(dest[1])-1][pos_dest] = board[int(orig[2])-1][pos_orig]
        board[int(orig[2])-1][pos_orig] = EMPTY



    for i in range(8,0,-1):
        print(i,board[i-1])
    print(" ",letras) 


    turno_lista[0],turno_lista[1]=turno_lista[1],turno_lista[0]


print("\nJugadas realizadas")
for i in range(len(historial_partida)):
    print(i+1,EMPTY,historial_partida[i])
    
    

    
    
    


