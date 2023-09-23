def is_simple(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


k = 0
for i in range(int(input())):
    if is_simple(int(input())):
        k += 1
print(k)
