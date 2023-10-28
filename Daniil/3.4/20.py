from itertools import *

s = input()
s = s.replace("->", ") <= (")
s = s.replace("~", " )) == ((")
s = "((" + s + "))"
perem = sorted(set([i for i in s if i.isupper()]))
print(*perem, "F")
for value in product(range(2), repeat=len(perem)):
    dct = dict(zip(perem, value))
    # print(dct)
    print(*value, int(eval(s, dct)))
