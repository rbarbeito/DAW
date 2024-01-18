diccionario = {}


# función que barre string y separa el texto teniendo en cuenta el patron enviado
def crear_lista(frase, patron):
    list=[]
    position = 0
    for i in range(len(frase)):
        if frase[i] == patron:
            list.append(frase[position:i])
            position = i+1
            
    # aquí adiciona el ultimo par o si es un solo par de valores creado
    list.append(frase[position:len(frase)])
    return list


datos_user = input(
    "Introduzca el juego de palabras (<ingles>:<español>) y cada una separada por comas: ")

list=crear_lista(datos_user,",")

for par in list:
    for i in range(len(par)):
        if par[i] == ":":
            diccionario[par[:i]] = par[i+1:]


frase=input("Teclee la frase a traducir: ")
list_frase=crear_lista(frase," ")

traduccion=""
for palabra in list_frase:
    if palabra in diccionario.keys():
        traduccion+=diccionario[palabra]+ " "
    else:
        traduccion+=" "
        
traduccion=traduccion[:len(traduccion)]

print(traduccion)     



