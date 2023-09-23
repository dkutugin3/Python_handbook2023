a = [int(input()) for i in range(3)]
a.sort(reverse=True)
if a[0] < (a[1] + a[2]):
    print("YES")
else:
    print("NO")
