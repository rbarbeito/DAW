# Problema 3 - Comprobación de la terminación de un número.
#   Dados dos enteros positivos a y b,tales que a>=b,el siguiente método calcula el número de cifras de b que 
#   aparecen como terminación de a. Es decir, calcula cuántas cifras consecutivas de b coinciden con consecutivas
#   cifras de a, leyendo las cifras de derecha a izquierda. Por ejemplo si a=8714509867 y b=9467, el método 
#   devuelve 2, dado que las dos últimas cifras de a coinciden con las de b.



while True:
    try:
        a = int(input("Entre el numero a: "))

        if a < 0:
            print("El numero debe ser positivo")
            continue
        else:
            break

    except ValueError:
        print("El valor debe ser un numero")

while True:
    try:
        b = int(input("Entre el numero b: "))

        if b > a :
            print("El numero debe ser menor que el numero a")
            continue
        elif b < 0:
            print("El numero debe ser positivo")
            continue
        else:
            break

    except ValueError:
        print("El valor debe ser un numero")
        
        
count=0

while True:
    if a%10 == b%10:
        count+=1
        a//=10
        b//=10
        continue
    break

print("Coincidencias:",count)
    