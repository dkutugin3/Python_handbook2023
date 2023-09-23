def solution():
    count = int(input())
    text = str(input())
    print(((f'Я больше никогда не буду писать "{text}"!' + "\n") * count)[:-1:])


def main():
    solution()


if __name__ == "__main__":
    main()
