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
    p = int(input()) - 1
    res = prime_div(int(input()))
    for i in range(p):
        a = prime_div(int(input()))
        i = 0
        while i < len(res):
            elem = res[i]
            if elem in a:
                a.pop(a.index(elem))
                i += 1
            else:
                res.pop(res.index(elem))

    answ = 1
    for elem in res:
        answ *= elem
    print(answ)


def main():
    solution()


if __name__ == "__main__":
    main()
