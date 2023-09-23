def solution():
    rows, columns = int(input()), int(input())
    lenght = len(str(rows * columns))
    for i in range(rows):
        for j in range(columns):
            print(f"{rows * j + i + 1: >{lenght}}", end=" ")
        print('')


def main():
    solution()


if __name__ == "__main__":
    main()
