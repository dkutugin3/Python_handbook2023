def solution():
    for a in (i := range(1, int(input()) + 1)):
        for b in i:
            print(f"{b} * {a} = {a * b}")


def main():
    solution()


if __name__ == "__main__":
    main()
