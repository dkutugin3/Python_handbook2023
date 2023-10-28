from itertools import product

n = range(1, 1 + int(input()))
k = 1
for i, j in product(n, repeat=2):
    if k % len(n) == 0:
        print(i * j, end="\n")
    else:
        print(i * j, end=" ")
    k += 1
