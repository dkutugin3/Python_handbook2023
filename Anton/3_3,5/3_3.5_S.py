from itertools import chain
import json
from sys import stdin
import os


def solution():
    bg_up = ord("A")
    en_up = ord("Z")
    bg_lw = ord("a")
    en_lw = ord("z")

    shift = int(input()) % 26
    ans = ''

    with open("public.txt", "r", encoding="UTF-8") as file:
        text = file.read()

    for symb in text:
        if bg_lw <= ord(symb) <= en_lw:
            if bg_lw <= ord(symb) + shift <= en_lw:
                ans += chr(ord(symb) + shift)
            elif ord(symb) + shift < bg_lw:
                ans += chr(en_lw + 1 - (bg_lw - (ord(symb) + shift)))
            elif ord(symb) + shift > en_lw:
                ans += chr(bg_lw - 1 + ((ord(symb) + shift) - en_lw))

        elif bg_up <= ord(symb) <= en_up:
            if bg_up <= ord(symb) + shift <= en_up:
                ans += chr(ord(symb) + shift)
            elif ord(symb) + shift < bg_up:
                ans += chr(en_up + 1 - (bg_up - (ord(symb) + shift)))
            elif ord(symb) + shift > en_up:
                ans += chr(bg_up - 1 + ((ord(symb) + shift) - en_up))

        else:
            ans += symb

    with open("private.txt", "w", encoding="UTF-8") as file:
        file.write(ans)


def main():
    solution()


if __name__ == "__main__":
    main()
