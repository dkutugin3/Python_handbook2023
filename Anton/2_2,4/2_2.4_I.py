def solution():
    answ = ''
    for i in range(int(input())):
        inp = str(max(list(map(int, str(input())))))
        answ += inp
    print(answ)


def main():
    solution()


if __name__ == "__main__":
    main()
