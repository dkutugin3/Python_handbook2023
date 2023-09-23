def solution():
    name = chr(ord('Я'))
    for i in range(int(input())):
        name = min(str(input()), name)
    print(name)


def main():
    solution()


if __name__ == "__main__":
    main()
