a = [int(i) for i in range(1, int(input()) + 1)]
k = 1
while True:
    if a:
        print(*a[:k])
        a = a[k:]
        k += 1
    else:
        exit()
