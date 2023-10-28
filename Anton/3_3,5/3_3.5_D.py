from sys import stdin


def solution():
    states = stdin.readlines()
    keyword = states.pop(-1).rstrip("\n ")
    print(*[state for state in states if keyword.lower() in state.lower()], sep="")


def main():
    solution()


if __name__ == "__main__":
    main()
