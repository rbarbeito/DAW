# lista =[[]]*3
# print(lista)
##
# lista[0].append(3)
# print(lista)
##
##
# lists = [[] for i in range(3)]
# print(lists)
##
# lists[0].append(3)
# print(lists)


# dictionario

# d = {"one": 1, "two": 2, "three": 3, "four": 4}
# print(d)
# print(list(d))
# print(list(d.values()))


# dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
# keys = dishes.keys()
# values = dishes.values()

# print(list(keys))

# del dishes['eggs']
# del dishes['sausage']

# print(list(keys))

# print(keys & {'eggs', 'bacon', 'salad'})


# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found a number", num)


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action,)
    print("if you put", voltage, "volts through it.",)
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

print(**d)
parrot(**d)
