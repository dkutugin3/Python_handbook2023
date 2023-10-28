from sys import stdin


def solution():
    for row in map(lambda x: x.split("#")[0].rstrip("\n ") + "\n" if x[0] != "#" else "", stdin.readlines()):
        print(row, end="")


def main():
    solution()


if __name__ == "__main__":
    main()
