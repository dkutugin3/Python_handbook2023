n = int(input())
m = int(input())
mx = len(str(n * m))
lst = [f"{' ' * (mx - len(str(i)))}{i}" for i in range(1, n * m + 1)]
rst = []
for i in range(m):
    rst.append(lst[i * n:n * (i + 1)])
rst2 = []
for i in range(len(rst)):
    if i % 2 == 0:
        rst2.append(sorted(rst[i]))
    else:
        rst2.append(sorted(rst[i], reverse=True))
for i in range(n):
    stroka = []
    for t in range(m):
        stroka.append(rst2[t][i])
    print(*stroka)
