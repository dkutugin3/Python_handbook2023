def solution():
    sides = tuple(int(input()) for i in range(3))
    if (sides[0] < sides[1] + sides[2]) and (sides[1] < sides[0] + sides[2]) and (sides[2] < sides[0] + sides[1]):
        print("YES")
    else:
        print("NO")


def main():
    solution()


if __name__ == "__main__":
    main()
