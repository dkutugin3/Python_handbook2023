def solution():
    year = int(input())
    if year % 100 != 0:
        if year % 4 == 0:
            print('YES')
        else:
            print('NO')
    else:
        if year % 400 == 0:
            print('YES')
        else:
            print('NO')


def main():
    solution()


if __name__ == "__main__":
    main()
