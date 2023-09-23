a = set()
n = int(input())
for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            if (i + j + k) == n:
                a.add((i, j, k))
a = [list(i) for i in a]
a.sort()
print("А Б В")
for i in a:
    print(*i)
