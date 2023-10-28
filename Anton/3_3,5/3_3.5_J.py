from itertools import chain
from sys import stdin


def solution():
    with open(input(), "r", encoding="UTF-8") as file:
        lines = list(map(lambda x: x.rstrip(" \n"), file.readlines()))
    n = int(input())
    for i in range(-n, 0):
        print(lines[i])


def main():
    solution()


if __name__ == "__main__":
    main()
