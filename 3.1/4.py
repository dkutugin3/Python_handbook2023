result = []
while a := input():
    if a[-3:] == "@@@":
        continue
    if a[:2] == "##":
        result.append(a[2:])
    else:
        result.append(a)
print(*result, sep="\n")
