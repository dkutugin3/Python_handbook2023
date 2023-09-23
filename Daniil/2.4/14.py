n = int(input())
m = int(input())
mx = len(str(n * m))
lst = [f"{' ' * (mx - len(str(i)))}{i}" for i in range(1, n * m + 1)]
for i in range(n):
    prnt = lst[m * i:m * (i + 1)]
    if i % 2 == 0:
        print(*prnt)
    else:
        prnt = prnt[::-1]
        print(*prnt)
