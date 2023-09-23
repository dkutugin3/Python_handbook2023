a = list(map(int, list(input())))
b = list(map(int, list(input())))
if len(a) != len(b):
    a = [0] * (max(len(a), len(b)) - len(a)) + a
    b = [0] * (max(len(a), len(b)) - len(b)) + b
res = [str((a[i] + b[i]) % 10) for i in range(len(a))]
print(int(''.join(res)))


