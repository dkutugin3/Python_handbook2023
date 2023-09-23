def solution():
    ans = []
    while (inp := str(input())) != "":
        inp = inp.split('#')
        if inp[0] != "":
            ans.append(inp[0])
    print(*ans, sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
