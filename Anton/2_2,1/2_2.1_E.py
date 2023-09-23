def solution():
    price = int(input())
    weight = int(input())
    note = int(input())
    print(note - int(price * weight))


def main():
    solution()


if __name__ == "__main__":
    main()