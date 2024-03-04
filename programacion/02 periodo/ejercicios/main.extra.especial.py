#a) Dado un string con parentesis limitadores, seleccionar el texto e invertir el string y quitar los paentisis
# b) invertir el orden de los string  fuera de los parentisis

# soluciones
# a) "hola(pepe de) mundo" debe quedar "hola ed epep mundo"
# b) "mundo ed epep hola"

texto="hola (pepe de) mundo"

position_inicial=0
position_final=0
contador=0

for i in texto:
    contador+=1
    if i=="(":
        position_inicial=contador
    elif i==")":
        position_final=contador
        
list_textos=[texto[:position_inicial-1],texto[position_inicial:position_final-1],texto[position_final:]]

# inverter=len(list_textos[1])
# texto_inverter=""
# while inverter !=0:
#     inverter-=1
#     texto_inverter+=list_textos[1][inverter]
    
list_textos[1]=list_textos[1][::-1]

if list_textos[0][len(list_textos[0])-1] ==" ":
    list_textos[0]=list_textos[0][:len(list_textos[0])-1]

if list_textos[2][0] ==" ":
    list_textos[2]=list_textos[2][1:]
    
    
for i in range(len(list_textos)):
    print(list_textos[i], end=" ")    
    
print()

list_textos[0],list_textos[2]=list_textos[2],list_textos[0]

for i in range(len(list_textos)):
    print(list_textos[i], end=" ")   