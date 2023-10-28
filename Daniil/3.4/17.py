from itertools import *

mst = input()
value = input()
mst_data = ["бубен", "пик", "треф", "червей"]
val_data = sorted([*map(str, range(2, 11)), "валет", "дама", "король", "туз"])
val_data.remove(value)
mst = [i for i in mst_data if i[0] == mst[0]][0]
old_data = " ".join(input().replace(",", "").split())
flag = 0
all_cards = [f"{i} {j}" for i, j in product(val_data, mst_data)]
for i, j, k in combinations(all_cards, 3):

    if flag and mst in i + " " + j + " " + k:
        print(i, j, k, sep=", ")
        break
    elif mst in i + " " + j + " " + k:
        now_card = i + " " + j + " " + k
        if now_card == old_data:
            flag = 1
