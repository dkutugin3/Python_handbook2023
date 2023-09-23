def solution():
    size, length = int(input()), int(input())
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            row.append(f"{i * j: ^{length}}")
        print(*row, sep='|')
        if i != size:
            print('-' * ((length + 1) * size - 1))


def main():
    solution()


if __name__ == "__main__":
    main()
