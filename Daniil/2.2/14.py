from itertools import permutations
a = str(int(input()))
res = []
for i, k in (permutations(a, r=2)):
    if i != "0":
        res.append(int(f"{i + k}"))
print(min(res), max(res))
