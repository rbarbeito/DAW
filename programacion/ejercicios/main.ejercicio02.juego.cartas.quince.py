import random
print("JUEGO DE CARTAS (QUINCE)")

cartas=[1,2,3,4,5,6,7,8,9,10]

hector_data=random.choices(cartas,k=3)
gloria_data=random.choices(cartas,k=3)

print("Gloria ha sacado:", gloria_data)
print("Hector ha sacado:", hector_data)

suma_hector=0
suma_gloria=0

for i in range(3):
    suma_gloria += gloria_data[i]
    suma_hector += hector_data[i]
    
        
if suma_hector>15 and suma_gloria>15:
    print("No ha ganado nadie")
elif suma_gloria > 15:
    print("Ganó Hector")
elif suma_hector > 15:
    print("Ganó Gloria")
elif suma_gloria > suma_hector:
    print("Ganó Gloria")
elif suma_gloria < suma_hector:
    print("Ganó Hector")
else:
    print("Han empatado")

    