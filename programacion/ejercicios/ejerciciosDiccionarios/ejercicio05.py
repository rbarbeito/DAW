diccionario = {}


# función que barre string y separa el texto teniendo en cuenta el patron enviado
def crear_lista(frase, patron):
    lista = []
    position = 0
    for i in range(len(frase)):
        if frase[i] == patron:
            lista.append(frase[position:i])
            position = i+1

    # aquí adiciona el ultimo par o si es un solo par de valores creado
    lista.append(frase[position:len(frase)])
    return lista


datos_user = input(
    "Introduzca el juego de palabras (<ingles>:<español>) y cada una separada por comas: ")

lista = crear_lista(datos_user, ",")

for par in lista:
    valores_pares = crear_lista(par, ":")

    diccionario[valores_pares[0]] = valores_pares[1]


print(diccionario)


frase = input("Teclee la frase a traducir: ")
list_frase = crear_lista(frase, " ")

traduccion = ""
for palabra in list_frase:
    if palabra in diccionario.keys():
        traduccion += diccionario[palabra] + " "
    else:
        traduccion += " "

traduccion = traduccion[:len(traduccion)]

print(traduccion)
