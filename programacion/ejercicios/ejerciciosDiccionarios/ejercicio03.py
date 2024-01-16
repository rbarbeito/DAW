frutas = {"Plátano": "1.35", "Manzana": "0.80", "Pera": "0.85", "Naranja": "0.70"}


while True:
    
    fruta=input("¿Que fruta compró?: ")
    
    if fruta=='':
        break
    
    if fruta not in frutas:
        print(fruta, "No se encuentra registrada")
        continue
    
    peso=input("¿Cuantos kilos de "+fruta+" compró?: ")
    
    if peso=='':
        break
    
    print("Usted debe pagar", float(peso)*float(frutas[fruta]))