def solution():
    digits = sorted(tuple(str(input())))
    if digits[0] != '0':
        n1 = digits[0] + digits[1]
    else:
        if digits[1] != '0':
            n1 = digits[1] + '0'
        else:
            n1 = digits[2] + '0'
    n2 = digits[2] + digits[1]
    print(n1, n2)


def main():
    solution()


if __name__ == "__main__":
    main()
