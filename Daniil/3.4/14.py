from itertools import *

a = sorted([input() for i in range(int(input()))])
for i in permutations(a, 3):
    print(*i, sep=", ")
