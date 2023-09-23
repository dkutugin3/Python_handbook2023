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
    print(*[i for i in prime_div(int(input()))], sep=" * ")


def main():
    solution()


if __name__ == "__main__":
    main()
