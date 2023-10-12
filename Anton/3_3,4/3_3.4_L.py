from itertools import *


def solution():
    n = int(input())
    print(*[f"{idx}. {item}" for (idx, item) in
            enumerate(sorted(chain.from_iterable([input().split(', ') for i in range(n)])), 1)], sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
