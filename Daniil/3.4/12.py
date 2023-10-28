from itertools import chain

a = enumerate(sorted(list(chain(*(input().replace(",", "").split() for i in range(int(input())))))), 1)
print(*[f"{i}. {j}" for i, j in a], sep="\n")
