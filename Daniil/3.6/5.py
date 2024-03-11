import json
import sys


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


lst = []
js_dict = dict()
for i in sys.stdin:
    i = i.rstrip("\n")
    lst.append(int(i))

primes = set()
for i in lst:
    if i >= 2:
        for k in range(2, i + 1):
            if i % k == 0:
                primes.add(k)

for i in primes:
    if is_prime(i):
        js_dict[i] = js_dict.get(i, [])
        for k in lst:
            if k % i == 0:
                js_dict[i].append(k)

for key, value in js_dict.items():
    js_dict[key] = sorted(set(value))
with open("result.json", mode="w", encoding="utf-8") as file:
    json.dump(js_dict, file, indent=4)
