from itertools import *


def solution():
    n = int(input())
    for it in permutations(sorted([input() for i in range(n)]), 3):
        print(*it, sep=', ')


def main():
    solution()


if __name__ == "__main__":
    main()
