# Calcular el factorial de un numero de manera recursiva e iterativo
# n! = n(n-1)(n-2)(n-3).....1

def factorial(n):
    fact = n
    if n <= 1:
        return 1
    else:
        for i in range(n-1, 0, -1):
            fact *= i

    return fact


def factorial_recursivo(n):
    if n <= 1:
        return 1
    return n*factorial_recursivo(n-1)


print("CALCULANDO EL FACTORIAL DE UN NÚMERO")
n = int(input("\nTeclee el numero deseado: "))
print("El factorial de", n, "con una función iterativa es", factorial(n))
print("El factorial de", n, "con una función recursiva es", factorial_recursivo(n))
