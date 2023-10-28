from sys import stdin
from itertools import chain


def pali_check(a: str):
    return a.lower() == a.lower()[::-1]


data = set(chain.from_iterable([i.rstrip("\n").split() for i in stdin]))
ans = [i for i in data if pali_check(i)]
print(*sorted(ans), sep="\n")
