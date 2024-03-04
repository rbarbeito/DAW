def is_prime(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
