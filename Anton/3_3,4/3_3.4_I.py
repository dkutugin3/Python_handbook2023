from itertools import *


def solution():
    n = int(input())
    print(*[f"{el} " if idx % n != n - 1 else f"{el}\n" for (idx, el) in
            enumerate([a * b for (a, b) in product(range(1, n + 1), repeat=2)])], sep='')


def main():
    solution()


if __name__ == "__main__":
    main()
