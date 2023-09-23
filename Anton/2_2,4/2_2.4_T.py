def sum_ss(x: int, base: int):
    x_based = ''
    answ = 0
    while x != 0:
        x_based += str(x % base)
        x //= base
    for i in x_based:
        answ += int(i)
    return answ


def solution():
    x = int(input())
    sums = [sum_ss(x, base) for base in range(2, 11)]
    maxi = 0
    pos = -1
    for i in range(len(sums)):
        if sums[i] > maxi:
            maxi = sums[i]
            pos = i + 2
    print(pos)


def main():
    solution()


if __name__ == "__main__":
    main()
