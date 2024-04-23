#!/usr/bin/pyhton3


def menuApp():
    menu=""



    long = 0
    for i in list_menu:
        if long < len(i[0]):
            long = len(i[0])

    long += 8

    print()
    print("*"*(long))
    print(" "*((long-len("Menú"))//2), "Menú", sep="")
    print("*"*(long))
    print()

    for i in range(len(list_menu)):
        print(" "*2, i+1, ". ", list_menu[i][0],  sep="")

    print(" "*2, "0. Salir",  sep="")
    print()
    print("*"*(long))

    return menu






if __name__=="__main__":
    print("Soy un modulo")

















