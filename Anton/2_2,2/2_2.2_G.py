def solution():
    num = str(input())
    if num[:2:] == num[:-3:-1]:
        print("YES")
    else:
        print("NO")


def main():
    solution()


if __name__ == "__main__":
    main()
