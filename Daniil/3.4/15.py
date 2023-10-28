from itertools import chain, permutations

a = sorted(list(chain(*(input().replace(",", "").split() for i in range(int(input()))))))
for i in permutations(a, 3):
    print(*i)
