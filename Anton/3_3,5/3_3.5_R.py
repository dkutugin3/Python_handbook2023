from itertools import chain
import json
from sys import stdin
import os


def solution():
    size = os.path.getsize(input())
    c = 0
    while size >= 1024:
        size = (size + 1023) // 1024
        c += 1
    match c:
        case 0:
            print(f'{size}Б')
        case 1:
            print(f'{size}КБ')
        case 2:
            print(f'{size}МБ')
        case 3:
            print(f'{size}ГБ')
        case _:
            print("ты че")


def main():
    solution()


if __name__ == "__main__":
    main()
