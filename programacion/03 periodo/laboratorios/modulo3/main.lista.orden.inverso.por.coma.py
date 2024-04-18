# ejercicio 2
margen_izquierdo = 4
titulo = "LISTA EN ORDEN INVERSO, SEPARADO POR COMAS"
long = len(titulo)+margen_izquierdo*2
print()
print("*"*long)
print(" "*margen_izquierdo + titulo)
print("*"*long)

list_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impresion = ""

# for i in range(len(list_numeros)):

#     # if len(list_numeros)-i-1 != 0:
#     #     print(list_numeros[len(list_numeros)-i-1], end=", ")
#     # else:
#     #     print(list_numeros[len(list_numeros)-i-1], end="")
#     impresion += str(list_numeros[len(list_numeros)-i-1])
#     if len(list_numeros)-i-1 > 0:
#         impresion += ", "

# print(impresion)

i = len(list_numeros)
while i > 1:
    print(list_numeros[i-1], end=", ")
    i -= 1

print(list_numeros[i-1], end=" ")
