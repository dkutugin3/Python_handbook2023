from itertools import chain
import json
from sys import stdin


def solution():
    with open(input(), "r", encoding="UTF-8") as file:
        nums = [el for el in chain.from_iterable(map(lambda x: x.rstrip("\n ").split(" "), file.readlines())) if
                el != ""]

        nums = list(map(int, nums))

    counter = {}

    for num in nums:
        counter["count"] = counter.get("count", 0) + 1
        if num > 0:
            counter["positive_count"] = counter.get("positive_count", 0) + 1

        counter["min"] = min(counter.get("min", float("inf")), num)
        counter["max"] = max(counter.get("max", -float("inf")), num)
        counter["sum"] = counter.get("sum", 0) + num

    counter["average"] = round(counter.get("sum", 0) / counter.get("count", 1), 2)

    with open(input(), "w", encoding="UTF-8") as output:
        json.dump(counter, output, ensure_ascii=False, indent=4)


def main():
    solution()


if __name__ == "__main__":
    main()
