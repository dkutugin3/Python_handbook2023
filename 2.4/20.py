def notation(n, cc):
    res = ""
    while n:
        res = str(n % cc) + res
        n //= cc
    return res


def sum_digits(n):
    n = map(int, list(str(n)))
    return sum(n)


ans = 0
num = int(input())
max_sum = 0
for i in range(10, 1, -1):
    if sum_digits(notation(num, i)) >= max_sum:
        max_sum = sum_digits(notation(num, i))
        ans = i
print(ans)
