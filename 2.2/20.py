a = [input() for i in range(3)]
a.sort()
for i in a:
    if "зайка" in i:
        print(i, len(i))
        exit()
