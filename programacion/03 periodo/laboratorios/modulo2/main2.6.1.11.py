cant_asteriscos = 80
print("*"*cant_asteriscos)
print("Programa para la hora final, con la hora\inicial y los minutos transcurridos")
print("*"*cant_asteriscos, "\n")


hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Cálculo de los horas y minutos a mostrar,
horas_mostrar = (hour + round(dura/60)) % 24
minutos_mostrar = (mins+dura) % 60


print("Hora final--> ", horas_mostrar, ":", minutos_mostrar)
