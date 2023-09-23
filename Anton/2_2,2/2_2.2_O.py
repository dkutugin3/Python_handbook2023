def solution():
    a = str(input())
    b = str(input())
    digits = tuple(map(int, (a[0], a[1], b[0], b[1])))
    max_dig = 0
    min_dig = 9
    for i in digits:
        if max_dig < i:
            max_dig = i
        if min_dig > i:
            min_dig = i
    res = max_dig * 100 + (sum(digits) - max_dig - min_dig) % 10 * 10 + min_dig
    print(res)


def main():
    solution()


if __name__ == "__main__":
    main()
