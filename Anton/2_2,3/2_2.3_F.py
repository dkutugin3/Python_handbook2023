def prime_div(x):
    div = 2
    divs = []
    while x != 1:
        if x % div == 0:
            divs.append(div)
            x //= div
        else:
            div += 1
    return divs


def solution():
    a = prime_div(int(input()))
    b = prime_div(int(input()))

    res = 1
    for i in a:
        if i in b:
            res *= i
            b.pop(b.index(i))
    print(res)


def main():
    solution()


if __name__ == "__main__":
    main()
