def solution():
    summ = 0
    for i in range(int(input())):
        summ += sum(tuple(map(int, str(input()))))
    print(summ)


def main():
    solution()


if __name__ == "__main__":
    main()
