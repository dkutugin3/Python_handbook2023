from itertools import *

a = sorted([input() for i in range(int(input()))])
for i in permutations(a, len(a)):
    print(*i, sep=", ")
