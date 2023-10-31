from itertools import chain

path1 = input()
path2 = input()
output = input()
with open(path1, encoding="utf-8", mode="r") as file:
    data1 = set(chain.from_iterable([i.rstrip("\n").split() for i in file]))
with open(path2, encoding="utf-8", mode="r") as file:
    data2 = set(chain.from_iterable([i.rstrip("\n").split() for i in file]))
with open(output, encoding="utf-8", mode="w") as file:
    print(*sorted(data1 ^ data2), file=file, sep="\n")
