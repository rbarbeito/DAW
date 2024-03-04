import random

print("JUEGO DE DADOS")

dados=[1,2,3,4,5,6]

carmen_dados=random.choices(dados,k=2)
david_dados=random.choices(dados,k=2)

print("Carmen:",carmen_dados, "David:", david_dados)

suma_carmen=0
suma_david=0

mayor_carmen=0
mayor_david=0


for i in range(2):
    suma_carmen+=carmen_dados[i]
    suma_david+=david_dados[i]
    
    if mayor_david > david_dados[i]:
        mayor_david = david_dados[i]
    
    if mayor_carmen > carmen_dados[i]:
        mayor_carmen = carmen_dados[i]

    
    
if suma_carmen > suma_david:
    print("Ha ganado Carmen")
elif suma_carmen < suma_david:
    print("Ha ganado David")
elif mayor_carmen > mayor_david:
    print("Ha ganado Carmen")
elif mayor_carmen< mayor_david: 
    print("Ha ganado David")
else:
    print("Han empatado")
    
    
