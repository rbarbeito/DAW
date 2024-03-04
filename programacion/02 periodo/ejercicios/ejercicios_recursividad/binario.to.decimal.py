
"""
The function `toDecimal` converts a binary number to its decimal equivalent.

:param numero: The variable "numero" represents the binary number that the user inputs
:param inicio: The parameter "inicio" represents the index of the current digit being processed in
the binary number. It starts with the index of the last digit in the binary number (len(binario)-1)
and decreases by 1 in each recursive call until it reaches 0
:param potencia: The parameter "potencia" represents the power of 2 that is being multiplied with
each digit of the binary number. It starts with a value of 0 and increases by 1 with each recursive
call
:param decimal: The parameter "decimal" is used to keep track of the decimal value of the binary
number as it is being converted. It starts with a value of 0 and is updated recursively as each
digit of the binary number is processed
:return: the decimal equivalent of the binary number entered by the user.
"""


def toDecimal(numero, inicio, potencia, decimal):

    if inicio < 0:
        return decimal

    if numero[inicio] == "1":
        # decimal = decimal + (2**potencia)
        return toDecimal(numero, inicio-1, potencia+1, decimal + (2**potencia))

    return toDecimal(numero, inicio-1, potencia+1, decimal)


binario = input("Teclea tu número binario: ")
print(toDecimal(binario, len(binario)-1, 0, 0))
