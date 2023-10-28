from itertools import *

s = input()
print("a b c f")
for a, b, c in product(range(2), repeat=3):
    print(a, b, c, int(eval(s)))
