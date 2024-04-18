# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4)
# y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes.
# Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.
margen_izquierdo = 4
titulo = "DIAS POR MESES"
long = len(titulo)+margen_izquierdo*2
print()
print("*"*long)
print(" "*margen_izquierdo + titulo)
print("*"*long)

lista_dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
lista_meses = ["enero", "febrero", "marzo", "abril", "mayo",
               "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

mes = int(input("Diga el número del mes desea obtener la información: "))

if mes > 12:
    print("El año solo tiene 12 meses")
elif mes < 1:
    print("Debe ser un numero mayor que cero")
else:
    print("El nombre del mes seleccionado es",
          lista_meses[mes-1], "tiene", lista_dias_meses[mes-1], "días")
