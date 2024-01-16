blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#	

height=0
seguir=True

while seguir:
    seguir=False
    
    if blocks >= height:
        height+=1
        blocks=blocks - height
        seguir=True
        if blocks < 0:
            height-=1

print("La altura de la pirámide:", height)
