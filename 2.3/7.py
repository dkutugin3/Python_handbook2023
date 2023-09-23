from math import gcd

a, b = int(input()), int(input())
print(a * b // gcd(a, b))
