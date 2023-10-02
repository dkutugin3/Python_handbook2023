def comp(x: list, y: list) -> list:
    if len(x) >= len(y):
        return x
    else:
        return y


def solution():
    counter = {}
    for i in range(int(input())):
        inp = str(input())
        if counter.get(inp, -1) != 0:
            counter[inp] = counter.get(inp, -1) + 1
        else:
            counter[inp] = 2

    print(*sorted(
        comp([elem[0] + ' - ' + str(elem[1]) for elem in counter.items() if elem[1] != 0], ["Однофамильцев нет"])),
          sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
