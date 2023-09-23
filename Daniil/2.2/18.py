a = [int(input()) ** 2 for i in range(3)]
a.sort()
if a[-1] == sum(a[:2]):
    print("100%")
    exit()
if a[-1] > sum(a[:2]):
    print("велика")
else:
    print("крайне мала")

