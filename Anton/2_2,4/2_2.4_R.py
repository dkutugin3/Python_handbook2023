def solution():
    rows = []
    i = 0
    n = 1
    length = 0
    stop = int(input())
    while i <= stop:
        row = []
        for j in range(n):
            i += 1
            if i > stop:
                break
            row.append(str(i))

        n += 1
        rows.append(row)
        length = max(length, len(' '.join(row)))
    for i in rows:
        print(f"{' '.join(i): ^{length}}")


def main():
    solution()


if __name__ == "__main__":
    main()
