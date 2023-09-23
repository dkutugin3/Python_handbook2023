def solution():
    counter = 0
    for i in range(int(input())):
        if 'зайка' in str(input()):
            counter += 1
    else:
        print(counter)


def main():
    solution()


if __name__ == "__main__":
    main()
