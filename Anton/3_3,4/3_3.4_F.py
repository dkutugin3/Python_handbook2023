from itertools import *


def solution():
    masti = ["пик", "треф", "бубен", "червей"]
    masti.remove(input())
    print(*chain.from_iterable([[f"{val} {mast}" for mast in masti] for val in
                                chain(range(2, 11), ("валет", "дама", "король", "туз"))]), sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
