def beauty(x: list, length: int) -> str:
    prod = []
    for i in x:
        prod.append(f"{i: ^{length + 1}}")
    return ''.join(prod)


def solution():
    n = int(input())
    length = len(str((n + 1) // 2))
    row = ['1'] * n
    cube = [beauty(row, length)]

    for i in range(1, (n + 1) // 2):
        row = row[0:i:] + [str(i + 1)] * (n - 2 * i) + row[-i::]
        cube.append(beauty(row, length))

    for j in range(n // 2):
        cube.append(cube[(n // 2) - 1 - j])

    print(*cube, sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
