result = [0 for i in range(1104)]
while (a := input()) != "ФИНИШ":
    a = a.lower()
    for i in a:
        result[ord(i)] += 1
a = result[65:]
print(chr(a.index(max(a)) + 65))
