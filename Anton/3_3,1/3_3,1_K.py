def solution():
    searches = []
    for i in range(int(input())):
        searches.append(str(input()))
    key = str(input())
    print(*[i for i in searches if (key.lower() in i.lower())], sep="\n")


def main():
    solution()


if __name__ == "__main__":
    main()
