a = [int(i) for i in range(1, int(input()) + 1)]
count = 1
result = []
while a:
    result.append(a[:count])
    a = a[count:]
    # print(a)
    count += 1
mx_len = len(" ".join(map(str, result[-1])))
for i in result:
    print(f"{' '.join(map(str, i)):^{mx_len}}")
