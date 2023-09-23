from itertools import product

a = [int(i) for i in range(1, int(input()) + 1)]
for i, k in product(a, a):
    print(f"{k} * {i} = {i * k}")
