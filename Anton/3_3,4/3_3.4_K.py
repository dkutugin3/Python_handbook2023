from itertools import *


def solution():
    n = int(input())
    m = int(input())
    print(*[f"{el: >{len(str(m * n))}} " if idx % m != m - 1 else f"{el: >{len(str(m * n))}}\n" for (idx, el) in
            enumerate([b + a * m for (a, b) in product(range(n), range(1, m + 1))])], sep='')


def main():
    solution()


if __name__ == "__main__":
    main()
