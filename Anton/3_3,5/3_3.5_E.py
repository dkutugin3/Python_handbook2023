from sys import stdin
from itertools import chain


def solution():
    words = chain.from_iterable(map(lambda x: x.rstrip("\n ").split(" "), stdin.readlines()))
    print(*sorted(list(set(
        [word for word in words if word.lower()[:len(word) // 2:] == word.lower()[-1:(len(word) - 1) // 2: -1]]))),
          sep="\n")


def main():
    solution()


if __name__ == "__main__":
    main()
