def solution():
    a = int(input())
    b = int(input())
    for i in range(a, b + 1 if a <= b else b - 1, -1 if a > b else 1):
        print(i, end=" ")


def main():
    solution()


if __name__ == "__main__":
    main()
