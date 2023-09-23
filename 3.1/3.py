length = int(input())
count = int(input())
result = []
for i in range(count):
    if len(a := input()) > length:
        result.append(a[:length - 3] + "...")
    else:
        result.append(a)
print(*result, sep="\n")
