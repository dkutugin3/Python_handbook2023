def solution():
    ans = []
    while (inp := str(input())) != "":
        if inp[-1:-4: -1] != "@@@":
            if inp[:2:] == "##":
                inp = inp[2::]
            ans.append(inp)
    print(*ans, sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
