diccionario={}

diccionario['nombre']='juan'
diccionario['edad']=25
diccionario['ciudad']='México'

print("\ndiccionario con valores: ",diccionario)

diccionario['edad']=30

print("\ndiccionario con nueva llave: ",diccionario)

del diccionario['ciudad']

print("\ndiccionario despues de elimanar llave: ",diccionario)

print ("\nkeys: ",diccionario.keys())
print ("\nvalues: ",diccionario.values())
print("\nitems: ",diccionario.items())

diccionario2={'carrera':'tech',"telefono":"0849077924","direccion":"calle de los vericuetos"}


print("\ndiccionario2: ",diccionario2)

diccionario_combinado = dict(diccionario, **diccionario2)


print("\ncombinado: ",diccionario_combinado)


print("\nlen combinado: ",len(diccionario_combinado))

print("\nEsta nombre en llaves?:", 'nombre' in diccionario_combinado.keys() )
print()

count=0
for clave, valor in diccionario_combinado.items():
    if clave[0] == "a" or clave[0] == "A":
        print ("llave con a: ", clave)
        count+=1

if count ==0:
    print("ninguna llave comienza con A")


count=0
print()
for clave, valor in diccionario_combinado.items():
    if type(valor) == int:
        print("Valor entero: ", valor)
        count+=1

if count==0:
    print("No hay valores de tipo entero en el diccionario")

diccionario_duplicado = diccionario_combinado.copy()
print("\nDiccionario duplicado: ", diccionario_duplicado)

diccionario_combinado.clear()

print("\nDiccionario_combinado Vacio: ", diccionario_combinado)

suma=0
for clave, valor in diccionario_duplicado.items():
    if type(valor)==int:
        suma+=valor

print("\nLa suma de los valores numericos de diccionario duplicado es:",suma)

concatenacion=""
for clave, valor in diccionario_duplicado.items():
    concatenacion+=clave+" "

print("\nConcatenacion de las llaves de diccionario_duplicado:",concatenacion)

diccionario_duplicado["vacia"]=""
diccionario_duplicado['cero']=0

count=0
print()
lista=[]

print(diccionario_duplicado)
for key, value in diccionario_duplicado.items():
    if value=="":
        lista.append(key)


for i in lista:
##    del diccionario_duplicado[i]
    diccionario_duplicado.pop(i)

print(diccionario_duplicado)
   


