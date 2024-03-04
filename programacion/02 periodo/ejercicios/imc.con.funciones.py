# Hacer un calcular de IMC teniendo en cuenta que los daos pueden estar en unidades métricas o inglesas,
# Hacer las funciones y las conversiones necesarias, asi como las validaciones de los datos

list_sistema = [
    "Cambiar a Sistema Anglosajón de Unidades (SAU)", "Cambiar a Sistema Internacional de Unidades (SIU)"]
sistema = [0, 1]
u_peso = ["Kg", "pounds"]
u_talla = ["m", "in"]
ciclo = True


def valida_peso(peso):
    return peso >= 20 and peso <= 200


def valida_altura(altura):
    return altura > 1 and altura < 2.5


def calcula_imc(peso, altura):
    return peso/altura**2


def pounds_kg(peso):
    return peso * 0.45359237


def inch_meters(altura):
    return altura * 0.0254


while ciclo:
    print("\n", "*"*10, sep="")
    print("MENU")
    print("*"*10)
    print("1. "+list_sistema[sistema[0]])
    print("2. Cálculo de IMC")
    print("0. Salir")

    menu = int(input("¿Qué eliges hacer? "))

    if menu == 0:
        break
    elif menu == 1:
        sistema[0], sistema[1] = sistema[1], sistema[0]
        u_peso[0], u_peso[1] = u_peso[1], u_peso[0]
        u_talla[0], u_talla[1] = u_talla[1], u_talla[0]

    elif menu == 2:
        peso = float(input("Introduzca el peso("+u_peso[0]+"): "))
        talla = float(input("Introduzca la talla("+u_talla[0]+"): "))

        if sistema[0] == 1:
            peso = pounds_kg(peso)
            talla = inch_meters(talla)

        if valida_peso(peso) == False:
            print("\n2** Error ** => El valor del peso esta fuera del rango valido")
            continue

        if valida_altura(talla) == False:
            print("\n2** Error ** => El valor de talla esta fuera del rango valido")
            continue

        imc = round(calcula_imc(peso, talla), 2)

        if imc < 18.5:
            print("\nBajo peso, su imc es", imc)
        elif 18.5 <= imc and imc <= 24.9:
            print("\nPeso normal, su imc es", imc)
        elif 25.0 <= imc and imc <= 29.9:
            print("\nSobrepeso, su imc es", imc)
        elif 30.0 <= imc:
            print("\nObesidad, su imc es", imc)


print("Gracias por usar nuestra aplicación - \xa9 CodeQba.com ")
