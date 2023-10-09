def solution():
    level1 = {}
    level2 = {}
    while (inp := str(input())) != "":
        inp = inp.split(' ')
        if level1.get(inp[1], set()) == set():
            level1[inp[1]] = set()
        if level1.get(inp[0], set()) == set():
            level1[inp[0]] = set()
        level1[inp[0]].add(inp[1])
        level1[inp[1]].add(inp[0])

    for elem in level1.items():
        for name in elem[1]:
            if level2.get(elem[0], set()) == set():
                level2[elem[0]] = set()
            level2[elem[0]] = level2[elem[0]].union(level1.get(name, set()))
        level2[elem[0]] = level2[elem[0]].difference({elem[0]}).difference(level1.get(elem[0], set()))

    for key in sorted(level2.keys()):
        print(key, end=": ")
        print(*sorted(list(level2[key])), sep=", ")


def main():
    solution()


if __name__ == "__main__":
    main()
