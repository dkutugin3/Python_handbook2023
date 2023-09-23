def solution():
    a = str(input())
    b = str(input())
    res = ''

    for i in range(-1, -(min(len(a), len(b))) - 1, -1):
        res += str((int(a[i]) + int(b[i])) % 10)

    ost = len(a) - len(b)
    if ost >= 0:
        res += a[:ost:][::-1]
    else:
        res += b[:abs(ost):][::-1]
    print(res[::-1])


def main():
    solution()


if __name__ == "__main__":
    main()
