from itertools import chain
import json
from sys import stdin


def solution():
    with open(name := input(), "r", encoding="UTF-8") as file:
        some_dict = json.load(file)

        for line in stdin.readlines():
            (key, value) = line.rstrip("\n ").split(" == ")
            some_dict[key] = value

    with open(name, "w", encoding="UTF-8") as file:
        json.dump(some_dict, file, ensure_ascii=False, indent=4)


def main():
    solution()


if __name__ == "__main__":
    main()
