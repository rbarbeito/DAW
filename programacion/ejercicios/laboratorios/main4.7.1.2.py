value = input('Ingresa un número natural: ')

is_number = True

for i in value:
    if i not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
        is_number = False
        print("No es un numero valido")
        break

if is_number:
    if value != 0:
        print('El recíproco de', value, 'es', 1/int(value))
    else:
        print("Division por cero no es posible")
