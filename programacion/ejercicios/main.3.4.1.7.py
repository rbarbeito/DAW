import random

lista_tuplas=[[-5.00,10.00],[8.00,30.00],[25.00,35.00],[20.00,30.00]]
temps=[]
##temps = [[round(random.uniform(-5.00, 35.5),2) for h in range(24)] for d in range(31)]
menor=0.00
mayor=0.00
total = 0.0
dias_temp_veinte_grados=0
semana_calurosa=0
semana_fria=0
contador_veinte=0

for i in range(31):
    lista_dia=[]
    for pos in lista_tuplas:
        for h in range(6):
            lista_dia.append(round(random.uniform(pos[0], pos[1]),2))
    temps.append(lista_dia)

for i in range(len(temps)):
    print(temps[i])

for day in temps:
   total += day[11]
   if day[11] > 20:
       dias_temp_veinte_grados+=1
   
for day in temps:
   for x in day:
       if x < menor:
            menor = x
       if x > mayor:
           mayor = x
           
           


print()
print("Menor es",menor)
print("Mayor es", mayor)
print("Temperatura promedio al mediodía:", round(total / 31,2))
print("Cantidad de dias con temperatura mayor a 20 grados:", dias_temp_veinte_grados)
