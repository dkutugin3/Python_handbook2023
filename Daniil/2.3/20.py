n = int(input())
B = [int(input()) for i in range(n)]


def check(n):
    b = B[n]
    m = b // (256 ** 2)
    b -= m * (256 ** 2)
    r = b // 256
    b -= r * 256
    if get_hash(n, m, r) != b or b >= 100:
        print(n)
        exit()


HASH = dict()


def get_hash(number, m=0, r=0):
    if number == 0:
        HASH[0] = (37 * (m + r)) % 256
        return HASH[0]
    else:
        HASH[number] = (37 * (m + r + HASH[number - 1])) % 256
        return HASH[number]


for i in range(n):
    check(i)
print(-1)