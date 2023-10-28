from sys import stdin


def solution():
    summ = 0
    count = 0
    for (name, prev_height, height) in map(lambda x: x.rstrip("\n").split(" "), stdin.readlines()):
        prev_height, height = int(prev_height), int(height)
        summ += height - prev_height
        count += 1
    print(round(summ / count))


def main():
    solution()


if __name__ == "__main__":
    main()
