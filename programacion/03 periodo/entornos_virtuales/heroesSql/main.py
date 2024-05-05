from functions.select import selectAll
from functions.super_heroe import SuperHeroe


def crearPersonaje():
    return selectAll()


listado = crearPersonaje()

for item in listado:
    personaje = SuperHeroe(item)


print('Cantidad de personajes: {}'.format(SuperHeroe.getCount()))

print('Personajes Buenos: {} - Personajes Malos: {} - Personajes Neutrales: {} - Personajes Desconocido: {}'.format(
        SuperHeroe.getCountGood(), SuperHeroe.getCountBad(), SuperHeroe.getCountNeutral(), SuperHeroe.getCountUnKnow()))

print('Cantidad de personales de Marvel Comics: {} - de DC Comics: {}'.format(
    SuperHeroe.getCountMarvelComic(),  SuperHeroe.getCountDcComic()))
