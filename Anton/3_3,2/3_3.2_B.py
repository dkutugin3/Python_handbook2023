def solution():
    print(*set(str(input())).intersection(set(str(input()))), sep="")


def main():
    solution()


if __name__ == "__main__":
    main()
