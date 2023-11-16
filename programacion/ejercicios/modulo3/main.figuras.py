print("Imprimiendo un cuadrado con *\n")
cant = int(input("Define cuanto astericos tendra el lado de su cuadrado: "))

rango = range(cant)

print('Pintamos cuadrado')
for i in rango:
    print("*  "*cant)

print("pintamos triangulo")

rango = range(cant+1)
for i in rango:
    print("*"*i)

print("pintamos tirangulo invertido")
num = cant
while num > 0:
    print("*"*num)
    num -= 1

maximo = cant*2+1

print("Pintamos el arbol")
rango_arbol = range(1, maximo, 2)
base = 0
for i in rango_arbol:
    espacios = (cant*2)-i//2
    print(" "*espacios, "*"*i, " "*espacios, sep="")
    base = i


rango_base = range(0, cant//2+1)
estrellas_base = (base//2)
espaciado = cant+(cant//2)

if cant % 2 != 0:
    estrellas_base = estrellas_base + 1

for i in rango_base:
    print(" "*espaciado, "*"*estrellas_base)

print("Pintamos un Rombo")
rango_rombo = range(1, maximo, 2)
for i in rango_rombo:
    espacios = (cant*2)-i//2
    print(" "*espacios, "*"*i, " "*espacios, sep="")

inverter_maximo = maximo
while inverter_maximo > 0:
    espacios = (cant*2)-inverter_maximo//2
    print(" "*espacios, "*"*inverter_maximo, " "*espacios, sep="")
    inverter_maximo -= 2
