# paso 1
Beatles = []


print("Paso 1:", Beatles)


# paso 2
Beatles.append("Jhon Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")

print("Paso 2:", Beatles)


# paso 3
cant = int(input("¿Cuantos nueos integrants vas adicionar: "))
for i in range(cant):
    nombre = input("Agregue un nombre a la banda: ")
    Beatles.append(nombre)


print("Paso 3:", Beatles)


# paso 4
del Beatles[3:]

print("Paso 4:", Beatles)


# paso 5
Beatles.insert(0, "Ringo Starr")

print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))
