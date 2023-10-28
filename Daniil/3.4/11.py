from itertools import product

n = int(input())
m = int(input())
mx_size = len(str(n * m))
for i in product(range(1, n * m + 1), repeat=1):
    if i[0] % m != 0:
        print(f"{i[0]:>{mx_size}}", end=" ")
    else:
        print(f"{i[0]:>{mx_size}}")
