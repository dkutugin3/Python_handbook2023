from itertools import *


def solution():
    mh_mast = input()[:3:]
    masti = ["бубен", "пик", "треф", "червей"]
    ex_val = input()
    values = chain(sorted(map(str, range(2, 11))), ["валет", "дама", "король", "туз"])
    cards = [f"{val} {mast}" for val, mast in product(values, masti)]

    i = 0
    for it in (combinations(cards, 3)):
        if i > 9:
            break
        it = ', '.join(it)
        if ex_val not in it and mh_mast in it:
            print(it)
            i += 1


def main():
    solution()


if __name__ == "__main__":
    main()
