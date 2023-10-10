from itertools import chain


def solution():
    n = int(input())
    print('А', 'Б', 'В')
    print(*chain.from_iterable([[f"{a} {b} {n - a - b}" for b in range(1, n - a)] for a in range(1, n - 1)]), sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
