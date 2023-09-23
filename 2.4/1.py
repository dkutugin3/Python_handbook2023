n = int(input())
ryad = [i * j for i in range(1, n + 1) for j in range(1, n + 1)]
for i in range(n):
    print(*ryad[i * n: n + i * n])