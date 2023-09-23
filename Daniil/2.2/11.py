a = input()
a = [int(i) for i in a]
a.sort()
if (a[0] + a[2]) == (a[1] * 2):
    print("YES")
else:
    print("NO")
