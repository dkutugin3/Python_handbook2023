a = [int(input()) for i in range(2)]
# a.sort()
if a[0] < a[1]:
    print(*(i for i in range(a[0], a[1] + 1)))
else:
    print(*(i for i in range(a[0], a[1] - 1, -1)))
