def solution():
    summ = 0
    while (inp := float(input())) != 0:
        summ += inp if inp < 500 else inp * 0.9
    print(summ)


def main():
    solution()


if __name__ == "__main__":
    main()
