from itertools import chain


def solution():
    print(
        *[f"{idx}. {purch}" for (idx, purch) in
          enumerate(sorted(chain.from_iterable([input().split(', ') for i in range(3)])), 1)],
        sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
