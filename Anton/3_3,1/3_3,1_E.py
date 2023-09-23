def solution():
    inp = str(input())
    if inp[:(len(inp) + 1) // 2:] == inp[:(len(inp) - 2) // 2:-1]:
        print("YES")
    else:
        print("NO")


def main():
    solution()


if __name__ == "__main__":
    main()
