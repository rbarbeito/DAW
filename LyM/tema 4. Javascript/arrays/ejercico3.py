import random
import math

lista = [
    {
        "nombre": "Rodolfo",
        "edad": 52,
        "preferencias": "MotoGp",
        "casado": True,
        "peso": 71,
        "amigos": ["Reda", "david", "raul", "jordi", "juanito"]
    },
    {
        "nombre": "Cristian",
        "edad": 15,
        "preferencias": "Volleyball",
        "casado": False,
        "peso": 60,
        "amigos": ["Reda", "Rodolfo"]
    },
    {
        "nombre": "Reda",
        "edad": 20,
        "preferencias": "Money",
        "casado": False,
        "peso": 55,
        "amigos": ["Cristian", "Rodolfo", "david", "raul"]
    }
]


def amigos(lista):
    mayores_edad=[]

    for i in range(len(lista)):
        if lista[i]["edad"]>=18:
            mayores_edad.append(lista[i])

    for i in range(len(mayores_edad)):
        aleatorio = math.floor(random.random()*len(mayores_edad[i]["amigos"]))

        print("El amigo aleatorio de", mayores_edad[i]["nombre"], "es:", mayores_edad[i]["amigos"][aleatorio])


amigos(lista)