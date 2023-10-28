from itertools import *

s = input()
perem = sorted(set([i for i in s.split() if len(i) == 1]))
print(*perem, "F")
for value in product(range(2), repeat=len(perem)):
    dct = dict(zip(perem, value))
    print(*value, int(eval(s, dct)))
