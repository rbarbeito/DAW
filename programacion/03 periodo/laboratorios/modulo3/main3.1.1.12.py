year = int(input("Introduce un año:"))

	
if year < 1582:
    print("No dentro del período del calendario Gregoriano")
    exit()
elif year%4 != 0:
    type_year="año común"
elif year%100 !=0:
    type_year="año bisiesto"
elif year%400 != 0:
    type_year="año común"
else:
    type_year="año bisiesto"
                        
print("El año: "+ str(year) +" es un "+  type_year)
    