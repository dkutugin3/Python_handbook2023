def solution():
    inp = str(input())
    i = 0
    while i < len(inp):
        if ord(inp[i]) % 2 == 0:
            inp = inp[:i:] + inp[i + 1::]
        else:
            i += 1
    print(inp)


def main():
    solution()


if __name__ == "__main__":
    main()
