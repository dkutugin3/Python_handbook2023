from itertools import product

n = int(input())
print("А Б В")
for i, j in product(range(1, n - 1), repeat=2):
    if i + j < n:
        print(f"{i} {j} {n - i - j}")
