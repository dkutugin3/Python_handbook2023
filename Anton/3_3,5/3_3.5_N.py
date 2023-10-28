from itertools import chain
import json
from sys import stdin


def solution():
    with open(name := input(), "r", encoding="UTF-8") as info:
        old = json.load(info)

    with open(input(), "r", encoding="UTF-8") as update:
        new = json.load(update)

    users = {}
    for user in old:
        users[user["name"]] = user
        del users[user["name"]]["name"]

    for user in new:
        for key in user.keys():
            if key != "name":
                users[user["name"]][key] = max(users[user["name"]].get(key, chr(0)), user.get(key))

    with open(name, "w", encoding="UTF-8") as info:
        json.dump(users, info, ensure_ascii=False, indent=4)


def main():
    solution()


if __name__ == "__main__":
    main()
