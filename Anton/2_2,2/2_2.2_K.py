def solution():
    num = tuple(map(int, str(input())))
    if (other := min(num) + max(num)) == (sum(num) - other) * 2:
        print("YES")
    else:
        print("NO")


def main():
    solution()


if __name__ == "__main__":
    main()
