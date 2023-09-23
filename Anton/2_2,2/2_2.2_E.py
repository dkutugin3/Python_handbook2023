def solution():
    n = int(input())
    m = int(input())
    n = n + 7 + 2 - 3
    m = m + 6 + 3 + 5 - 2
    if n > m:
        print('Петя')
    else:
        print("Вася")


def main():
    solution()


if __name__ == "__main__":
    main()
