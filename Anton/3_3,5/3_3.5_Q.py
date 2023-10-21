from itertools import chain
import json
from sys import stdin


def solution():
    with open("public.txt", 'r', encoding="UTF-8") as file:
        out = ''.join([chr(ord(char) % 128) for char in file.read()])
    print(out)


def main():
    solution()


if __name__ == "__main__":
    main()
