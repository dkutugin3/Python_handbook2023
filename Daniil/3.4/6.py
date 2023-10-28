from itertools import product

masti = ["пик", "треф", "бубен", "червей"]
nominal = [*map(str, range(2, 11)), "валет", "дама", "король", "туз"]
exc = input()
masti = [i for i in masti if i != exc]
for i, j in product(nominal, masti):
    print(f"{i} {j}")
