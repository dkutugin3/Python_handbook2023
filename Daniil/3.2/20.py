from math import gcd

s = input()
s = s.replace(";", "")
s = sorted(set((map(int, s.split()))))
for i in s:
    relatively_prime = sorted([k for k in s if gcd(k, i) == 1])
    if relatively_prime:
        print(f"{i} - ", end="")
        print(*relatively_prime, sep=", ")
