from itertools import *


def solution():
    print(*[f"{lt} - {rt}" for (lt, rt) in combinations([input() for i in range(int(input()))], 2)], sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
