from itertools import chain
import json
from sys import stdin
import os


def solution():
    ans = 0

    with open('numbers.num', 'rb') as file:
        while b := file.read(2):
            ans += int.from_bytes(b)
    print(ans % 2 ** 16)


def main():
    solution()


if __name__ == "__main__":
    main()
