# Dado a un array de char y un char c, el siguiente método escribe en la salida
# estándar los sucesivos prefijos de a, de más corto a más largo, que no
# contienen el carácter c.
test = [0 for i in range(14)]
count = 1
i = 0

while i < len(test):
    test[i] = count

    if i == 0:
        i = len(test) // 2
    else:
        i += len(test[i:])//2+1

    count += 1
    print(test)
print(test)
