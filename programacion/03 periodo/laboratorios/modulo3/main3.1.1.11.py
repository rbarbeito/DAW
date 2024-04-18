income = float(input("Introduce el ingreso anual:"))
exencion_fiscal=85528

if income <= exencion_fiscal:
    tax=(income*0.18)-556.2
elif income:
    tax=14839.2 + ((income-exencion_fiscal)*0.32)

if tax < 0:
    tax = 0.0

    
    

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
