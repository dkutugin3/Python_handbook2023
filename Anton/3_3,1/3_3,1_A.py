def solution():
    ans = True
    for i in range(int(input())):
        inp = str(input())
        ans = ans and ((ord(inp[0]) >= ord('а')) and (ord(inp[0]) <= ord('в')))

    if ans:
        print("YES")
    else:
        print("NO")


def main():
    solution()


if __name__ == "__main__":
    main()
