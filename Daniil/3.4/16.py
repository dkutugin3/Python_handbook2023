from itertools import *

mst = input()
value = input()
mst_data = sorted(["бубен", "пик", "треф", "червей"])
val_data = sorted([*map(str, range(2, 11)), "валет", "дама", "король", "туз"])
val_data.remove(value)
mst = [i for i in mst_data if i[0] == mst[0]][0]
c = 0
all_cards = product(val_data, mst_data)
for i, j, k in combinations(all_cards, 3):
    if mst in [*i, *j, *k] and c < 10:
        print(*[f"{p[0]} {p[1]}" for p in (i, j, k)], sep=", ")
        c += 1
