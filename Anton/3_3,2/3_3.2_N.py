def comp(x: list, y: list) -> list:
    if len(x) >= len(y):
        return x
    else:
        return y


def solution():
    ingr = {}
    ans = []
    for n in range(int(input())):
        ingr[str(input())] = True
    for m in range(int(input())):
        inp = str(input())
        ans.append(inp)
        for c in range(int(input())):
            if not ingr.get(str(input()), False):
                try:
                    ans.remove(inp)
                except ValueError:
                    pass

    print(*sorted(comp(ans, ["Готовить нечего"])), sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
