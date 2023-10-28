from sys import stdin


def solution():
    nums = []
    for line in stdin:
        nums += [num for num in map(int, line.rstrip("\n ").split(' '))]

    print(sum(nums))


def main():
    solution()


if __name__ == "__main__":
    main()
