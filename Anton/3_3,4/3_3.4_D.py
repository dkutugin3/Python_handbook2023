from itertools import accumulate


def solution():
    print(*[' '.join(row) for row in accumulate([[word] for word in input().split(' ')])], sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
