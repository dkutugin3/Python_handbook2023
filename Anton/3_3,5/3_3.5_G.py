from itertools import chain
from sys import stdin


def solution():
    with open(input(), "r", encoding="UTF-8") as file:
        nums = list(map(int, chain.from_iterable(map(lambda x: x.rstrip("\n ").split(" "), file.readlines()))))
    counter = {}
    min_ = float('inf')
    max_ = -float('inf')

    for num in nums:
        counter["count"] = counter.get("count", 0) + 1
        if num > 0:
            counter["pos"] = counter.get("pos", 0) + 1
        counter["summ"] = counter.get("summ", 0) + num
        min_ = min(min_, num)
        max_ = max(max_, num)

    print(counter["count"], counter["pos"], min_, max_, counter["summ"],
          f"{counter['summ'] / counter['count'] :.2f}",
          sep="\n")


def main():
    solution()


if __name__ == "__main__":
    main()
