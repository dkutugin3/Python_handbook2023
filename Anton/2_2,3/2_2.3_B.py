def solution():
    counter = 0
    while (inp := str(input())) != "Приехали!":
        if 'зайка' in inp:
            counter += 1
    else:
        print(counter)


def main():
    solution()


if __name__ == "__main__":
    main()
