a = [list(input()) for i in range(3)]
a0 = set(i[0] for i in a)
a1 = set(i[1] for i in a)
if len(a0) == 1:
    print(*a0)
else:
    print(*a1)