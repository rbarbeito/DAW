# calcular el fibonachi de un numero

def fibo(numero):
    lst = [0, 1]
    for n in range(2, numero+1):
        lst.append(lst[n-2]+lst[n-1])

    print(lst)
    return lst[numero]


def fibo_recursiva(n):
    if n <= 1:
        return n
    else:
        return fibo_recursiva(n-1)+fibo_recursiva(n-2)


num = int(input("Numero a calcular: "))
print(fibo(num))
print(fibo_recursiva(num))
