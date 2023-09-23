a = [int(input()) for i in range(2)]
a.sort()
print(*(i for i in range(a[0], a[1] + 1)))