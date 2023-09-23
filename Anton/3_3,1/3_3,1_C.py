def solution():
    length = int(input())
    for i in range(int(input())):
        inp = str(input())
        if len(inp) > length:
            inp = inp[:length - 3:] + '...'
        print(inp)


def main():
    solution()


if __name__ == "__main__":
    main()
