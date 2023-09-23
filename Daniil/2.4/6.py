from math import gcd
n = int(input())
print(gcd(*tuple(int(input()) for i in range(n))))