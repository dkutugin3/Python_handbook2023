from itertools import chain, product, combinations


def solution():
    mh_mast = input()[:3:]
    masti = ["бубен", "пик", "треф", "червей"]
    ex_val = input()
    prev = input()
    values = chain(sorted(map(str, range(2, 11))), ["валет", "дама", "король", "туз"])
    cards = [f"{val} {mast}" for val, mast in product(values, masti)]

    last_it = ''
    for it in (combinations(cards, 3)):
        it = ', '.join(it)
        if ex_val not in it and mh_mast in it:
            if last_it == prev:
                print(it)
                break
            last_it = it


def main():
    solution()


if __name__ == "__main__":
    main()
