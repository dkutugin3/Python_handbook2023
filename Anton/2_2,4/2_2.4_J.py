def solution():
    count = int(input())
    print('А', 'Б', 'В')
    for a in range(1, count - 1):
        for b in range(1, count - a):
            print(a, b, count - a - b)


def main():
    solution()


if __name__ == "__main__":
    main()
