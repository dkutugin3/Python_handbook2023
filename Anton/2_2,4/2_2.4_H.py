def solution():
    counter = []
    for i in range(int(input())):
        counter.append(tuple([chr(i) + str(input()), sum(tuple(map(int, str(input()))))][::-1]))

    print(sorted(counter)[-1][1][1::])


def main():
    solution()


if __name__ == "__main__":
    main()
