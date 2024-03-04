divisas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

while True:
    
    pregunta=input("¿Qué divisa deseas consultar?: ")
    
    if pregunta=='':
        break
    
    if pregunta not in divisas:
        print("Esa divisa no esta registrada")
    else:
        print("El símbolo es:", divisas[pregunta])