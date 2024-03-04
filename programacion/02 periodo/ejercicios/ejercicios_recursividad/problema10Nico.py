test = [0 for i in range(100)]
count = 1
i= 0
while i < len(test):
    test[i] = count
    if i == 0:
        i = len(test) // 2
    else:
        i += len(test[i:])//2 + 1


    count+=1
print(test)
