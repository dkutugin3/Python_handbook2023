def solution():
    ans = set()
    for i in range(int(input())):
        ans = ans.union(set(str(input()).split(" ")))
    print(*ans, sep="\n")


def main():
    solution()


if __name__ == "__main__":
    main()
