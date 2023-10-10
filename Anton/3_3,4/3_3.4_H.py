from itertools import *


def solution():
    print(*islice(cycle([input() for i in range(int(input()))]), 0, int(input())), sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
