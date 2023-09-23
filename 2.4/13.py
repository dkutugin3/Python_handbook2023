n = int(input())
m = int(input())
mx = len(str(n * m))
lst = [f"{' ' * (mx - len(str(i)))}{i}" for i in range(1, n * m + 1)]
for i in range(n):
    print(*lst[i::n])
