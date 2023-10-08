def solution():
    cords = {}
    for n in range(int(input())):
        (x, y) = tuple(map(int, str(input()).split(' ')))
        key = str(x // 10) + ' ' + str(y // 10)
        cords[key] = cords.get(key, 0) + 1
    print(max(cords.values()))


def main():
    solution()


if __name__ == "__main__":
    main()
