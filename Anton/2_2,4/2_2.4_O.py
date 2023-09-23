def solution():
    rows, columns = int(input()), int(input())
    lenght = len(str(rows * columns))
    for i in range(rows):
        for j in range(columns):
            if j % 2 == 0:
                print(f"{i + 1 + (j // 2 * (2 * rows)): >{lenght}}", end=" ")
            else:
                print(f"{-i + ((j // 2 + 1) * (2 * rows)): >{lenght}}", end=' ')
        print('')


def main():
    solution()


if __name__ == "__main__":
    main()
