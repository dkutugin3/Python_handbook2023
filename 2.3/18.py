def is_simple(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


def simple_list(n):
    res = []
    for i in range(1, int(n ** 0.5) + 2):
        if is_simple(i):
            while n % i == 0:
                res.append(i)
                n //= i
    if n != 1:
        res.append(n)
    return sorted(res)


print(*simple_list(int(input())), sep=" * ")
