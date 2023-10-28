from itertools import chain
from sys import stdin


def solution():
    words = set()
    for i in range(2):
        with open(input(), "r", encoding="UTF-8") as file:
            words = words.symmetric_difference(
                set(chain.from_iterable(map(lambda x: x.rstrip("\n ").split(" "), file.readlines()))))
    with open(input(), "w", encoding="UTF-8") as ans:
        for word in sorted(list(words)):
            ans.write(str(word) + "\n")


def main():
    solution()


if __name__ == "__main__":
    main()
