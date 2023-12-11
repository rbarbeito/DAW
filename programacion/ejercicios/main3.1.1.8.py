asteriscos=50
print("*"*asteriscos,"\n Intentamos obtener el numero mayor de 3 numeros\n","*"*asteriscos)


number1=int(input("Entre el primer numero:"))
number2=int(input("Entre el segundo numero:"))
number3=int(input("Entre el tercer numero:"))

numero_mayor=number1

if numero_mayor < number2:
    numero_mayor = number2
    
if numero_mayor < number3:
    numero_mayor = number3

print("El numero mayor es: ", numero_mayor)
    