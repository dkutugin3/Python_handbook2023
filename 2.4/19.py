n = int(input())
res = [0 for i in range(n)]
res = [res[:] for i in range(n)]
mx = 0
for i in range(n):
    for j in range(n):
        res[j][i] = min(i + 1, j + 1, n - i, n - j)
        mx = max(mx, min(i + 1, j + 1, n - i, n - j))
mx = len(str(mx))
for i in res:
    prnt = ''
    for j in i:
        prnt += "{:>{}} ".format(j, mx)
    print(prnt[:-1])
