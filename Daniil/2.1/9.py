n = int(input())
m = int(input())
if n % 2 == 1:
    n -= 1
n = n // 2
print(m * n)