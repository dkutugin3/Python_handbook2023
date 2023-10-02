def solution():
    counter = {}
    for i in range(int(input())):
        inp = str(input())
        if counter.get(inp, -1) != 0:
            counter[inp] = counter.get(inp, -1) + 1
        else:
            counter[inp] = 2
    print(sum(counter.values()))


def main():
    solution()


if __name__ == "__main__":
    main()
