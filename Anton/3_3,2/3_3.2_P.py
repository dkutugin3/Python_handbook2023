def solution():
    ans = set()
    while (inp := str(input())) != '':
        inp = inp.split(' ')
        for idx, elem in enumerate(inp):
            if elem == "зайка":
                try:
                    ans.add(inp[idx + 1])
                except IndexError:
                    pass
                ans.add(inp[abs(idx - 1)])
    print(*ans, sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
