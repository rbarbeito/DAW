list = []

while True:
    numero = int(input('Adicionamos números hasta que teclees "-1": '))

    if numero != -1:
        list.append(numero)
    else:
        print("No adicionamos más números, aqui ests tu lista creada")
        print(list)
        break

# count = len(list)
# print(count)

for i in range(len(list)//2):
    # for i in range(count):
    # count -= 1
    # if count > 0:
    # list[i], list[count] = list[count], list[i]
    list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]

print("Aqui esta tu lista invertida:", list)
