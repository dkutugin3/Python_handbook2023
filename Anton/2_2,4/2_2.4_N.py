def solution():
    rows, columns = int(input()), int(input())
    lenght = len(str(rows * columns))
    for i in range(rows):
        for j in range(columns):
            if i % 2 == 0:
                print(f"{j + 1 + (i // 2 * (2 * columns)): >{lenght}}", end=" ")
            else:
                print(f"{-j + ((i // 2 + 1) * (2 * columns)): >{lenght}}", end=' ')
        print('')


def main():
    solution()


if __name__ == "__main__":
    main()
