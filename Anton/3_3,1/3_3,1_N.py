def solution():
    nums = str(input()).split(" ")
    power = int(input())
    print(*tuple(map(lambda x: int(x) ** power, nums)))


def main():
    solution()


if __name__ == "__main__":
    main()
