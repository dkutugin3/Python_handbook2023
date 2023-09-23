result = []
while (a := input()):
    a = a.split("#")[0]
    if a:
        result.append(a)
print(*result, sep="\n")
