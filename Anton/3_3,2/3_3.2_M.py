def comp(x: list, y: list) -> list:
    if len(x) >= len(y):
        return x
    else:
        return y


def solution():
    possible = set(str(input()) for n in range(int(input())))
    alr_cooked = set()
    for m in range(int(input())):
        for c in range(int(input())):
            alr_cooked.add(str(input()))
    print(*sorted(comp(list(possible.difference(alr_cooked)), ["Готовить нечего"])), sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
