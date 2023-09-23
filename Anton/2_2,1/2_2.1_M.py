def solution():
    children = int(input())
    candies = int(input())

    print(str(candies // children) + "\n" +
          str(candies % children))


def main():
    solution()


if __name__ == "__main__":
    main()
