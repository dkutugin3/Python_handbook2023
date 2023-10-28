from itertools import chain
import json
from sys import stdin


def solution():
    total = 0
    with open("scoring.json", "r", encoding="UTF-8") as scoring:
        sc = json.load(scoring)

    for group in sc:
        corr = 0
        count = 0
        for test in group["tests"]:
            if test["pattern"] == input():
                corr += 1
            count += 1
        total += group["points"] * corr // count

    print(total)


def main():
    solution()


if __name__ == "__main__":
    main()
