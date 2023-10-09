from itertools import count


def solution():
    (begin, end, step) = tuple(map(float, input().split()))
    for value in count(begin, step):
        if value > end:
            break
        else:
            print(f"{value:.2f}")


def main():
    solution()


if __name__ == "__main__":
    main()
