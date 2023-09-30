def solution():
    ans = set()
    n = int(input())
    m = int(input())
    for i in range(n + m):
        if (inp := str(input())) not in ans:
            ans.add(inp)
        else:
            ans.remove(inp)

    if not ans:
        print("Таких нет")
    else:
        print(len(ans))


def main():
    solution()


if __name__ == "__main__":
    main()
