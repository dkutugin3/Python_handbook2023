def solution():
    a = float(input())
    b = float(input())
    c = float(input())
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
        if a < b:
            a, b = b, a
    if a ** 2 < b ** 2 + c ** 2:
        print('крайне мала')
    elif a ** 2 == b ** 2 + c ** 2:
        print('100%')
    else:
        print('велика')


def main():
    solution()


if __name__ == "__main__":
    main()
