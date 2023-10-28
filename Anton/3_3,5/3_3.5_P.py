from itertools import chain
import json
from sys import stdin


def solution():
    search = ''.join(input().lower().split(' '))
    ans = ''

    for file_name in stdin:
        with open(file_name.rstrip('\n'), "r", encoding="UTF-8") as file:
            text = ''.join([word for word in chain.from_iterable(
                [elem.split("\t") for elem in
                 chain.from_iterable([row.split(' ') for row in file.read().split("\n")])])]).lower()
        if search in text:
            ans += file_name

    print(ans if ans != '' else "404. Not Found")


def main():
    solution()


if __name__ == "__main__":
    main()
